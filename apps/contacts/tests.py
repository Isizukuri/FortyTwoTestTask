from django.test import TestCase, Client

from apps.contacts.models import Contact


class TestHomePage(TestCase):
    """Test for contacts homepage"""
    def setUp(self):
        self.client = Client()
        self.url = reverse('home')

    def test_status(self):
        """Test response status"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        """Check used template"""
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'contacts/index.html')

    def test_assert_other_data_at_page(self):
        """Check present all contacts data on the home page"""
        response = self.client.get(self.url)
        self.assertIn('Name:', response.content)
        self.assertIn('Last name:', response.content)
        self.assertIn('Date of birth:', response.content)
        self.assertIn('Bio:', response.content)
        self.assertIn('Contacts:', response.content)
        self.assertIn('Email:', response.content)
        self.assertIn('Jabber:', response.content)
        self.assertIn('Skype:', response.content)
        self.assertIn('Other contacts:', response.content)

    def test_context_data(self):
        """..."""
#        response.context['object_list'][0]
        pass

    def test_no_text_notes(self):
        """Test in case if there are no contact data""""
        Contact.objects.all().delete()
        response = self.client.get(self.url)
        self.assertContains(response, 'No contact data.')