from django.test import TestCase

from models import LastRequest


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
        for i in xrange(3):
            self.client.get(reverse('home'))

        self.assertEqual(LastRequest.objects.count(), 3)
        self.assertEqual(
            LastRequest.objects.first().url,
            reverse('home'),
        )
        self.assertEqual(
            LastRequest.objects.all()[1].url, reverse('home'))
