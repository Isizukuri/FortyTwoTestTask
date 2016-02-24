from django.db import models
from django.utils.translation import ugettext_lazy as _


class Contact(models.Model):
    """Model to store contact info"""
    first_name = models.CharField(
        max_length=15,
        verbose_name=_('first name'),
        blank=False,
        )

    last_name = models.CharField(
        max_length=15,
        verbose_name=_('last name'),
        blank=False,
        null=True,
        )

    birth_date = models.DateField(
        verbose_name=_('birth date'),
        null=True,
        blank=True,
        )

    email = models.EmailField(
        verbose_name=_('email'),
        null=False,
        blank=False,
        )

    jabber = models.EmailField(
        verbose_name=_('jabber'),
        null=True,
        blank=True,
        )

    skype = models.CharField(
        max_length=40,
        verbose_name=_('skype'),
        null=True,
        blank=True,
        )

    bio = models.TextField(
        verbose_name=_('bio'),
        null=True,
        blank=True,
        )

    other_contacts = models.TextField(
        verbose_name=_('other contact'),
        null=True,
        blank=True,
        )

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')

    def __str__(self):
        return "{0}".format(self.email)
