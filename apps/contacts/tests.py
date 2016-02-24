from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from .models import Contact


class TextNoteModelTest(TestCase):
    """Test for Contact model"""
    def test_unicode_representation(self):
        """..."""
        contact = Contact(first_name="Luke", email="luke.skywalker@jedi.com")
        self.assertEqual(unicode(contact), contact.email)


class TestHomePage(TestCase):
    """Test for contacts homepage"""
    def setUp(self):
        self.client = Client()
        self.url = reverse('home')
        contact_data = dict(
            first_name='Luke',
            last_name='Skywalker',
            email='luke.skywalker@jedi.com'
        )
        contact = Contact(**contact_data)
        contact.save()

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
        self.assertIn('Contacts', response.content)
        self.assertIn('Email:', response.content)
        self.assertIn('Jabber:', response.content)
        self.assertIn('Skype:', response.content)
        self.assertIn('Other contacts:', response.content)

    def test_context_data(self):
        """..."""
        response = self.client.get(self.url)
        test_object = response.context['object']
        self.assertEqual(Contact.objects.first(), test_object)

    def test_no_text_notes(self):
        """Test in case if there are no contact data"""
        Contact.objects.all().delete()
        response = self.client.get(self.url)
        self.assertContains(response, 'No contact data.')
