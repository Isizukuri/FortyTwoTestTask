from django.db import models
from django.utils.translation import ugettext_lazy as _


class LastRequest(models.Model):
    """Table to store user last requests"""
    url = models.CharField(max_length=120)
    method = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{time}, url: {url}, method: {method}'.format(
            time=self.timestamp,
            url=self.url,
            method=self.method
            )
