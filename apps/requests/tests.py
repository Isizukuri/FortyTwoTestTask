from django.test import TestCase

from models import TextNote, LastRequest


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

