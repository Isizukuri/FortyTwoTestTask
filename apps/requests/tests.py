import json

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.conf import settings

from .models import LastRequest


class TextNoteModelTest(TestCase):
    """Test for LastRequest model"""
    def test_unicode_representation(self):
        """..."""
        last_request = LastRequest(url='/', method='GET')
        last_request.save()
        representation = '{time}, url: {url}, method: {method}'.format(
            time=last_request.timestamp,
            url=last_request.url,
            method=last_request.method
        )
        self.assertEqual(unicode(last_request), representation)


class MiddlewareTest(TestCase):
    """Test for custom middleware"""
    def test_common_requests(self):
        """common middleware test"""
        for i in xrange(3):
            self.client.get(reverse('home'))

        self.assertEqual(LastRequest.objects.count(), 3)
        self.assertEqual(
            LastRequest.objects.first().url,
            reverse('home'),
        )
        self.assertEqual(
            LastRequest.objects.all()[1].url, reverse('home'))

    def test_excluded_requests(self):
        """test middleware exclusions"""
        self.client.get(reverse('admin:jsi18n'))
        self.client.get(settings.MEDIA_URL)
        self.client.get(settings.STATIC_URL)
        self.client.get(
            reverse('last_requests'),
            HTTP_X_REQUESTED_WITH='XMLHttpRequest',
        )
        self.assertEqual(LastRequest.objects.count(), 0)


class RequestListViewTest(TestCase):
    """Test for view, that displays last 10 requests"""
    def test_status(self):
        """..."""
        response = self.client.get(reverse('last_requests'))
        self.assertEqual(response.status_code, 200)

    def test_queryset_with_less_then_10_entries(self):
        """..."""
        for i in xrange(3):
            response = self.client.get(reverse('last_requests'))
        self.assertEqual(len(response.context['object_list']), 3)
        self.assertQuerysetEqual(
            response.context['object_list'],
            map(repr, LastRequest.objects.all().order_by('-timestamp')[:10])
        )

    def test_queryset_with_more_then_10_entries(self):
        """..."""
        for i in xrange(25):
            response = self.client.get(reverse('last_requests'))
        self.assertEqual(len(response.context['object_list']), 10)
        self.assertQuerysetEqual(
            response.context['object_list'],
            map(repr, LastRequest.objects.all().order_by('-timestamp')[:10])
        )

    def test_ajax_response_without_request_entries(self):
        """..."""
        response = self.client.get(
            reverse('last_requests'), HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(len(json.loads(response.content)), 1)
        message = json.dumps({'error': 'There are no requests at all.'})
        self.assertJSONEqual(message, response.content)

    def test_ajax_response_with_10_entries(self):
        """..."""
        for i in xrange(10):
            self.client.get(reverse('home'))
        response = self.client.get(
            reverse('last_requests'), HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(len(json.loads(response.content)), 10)
