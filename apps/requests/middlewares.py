from django.core.urlresolvers import reverse
from django.conf import settings

from .models import LastRequest


class RequestStoreMiddleware(object):
    """Middleware to store http requests in database"""
    def process_request(self, request):
        path_info = request.META['PATH_INFO']
        last_request = LastRequest(
            url=request.META['PATH_INFO'],
            method=request.META['REQUEST_METHOD'],
            )
        last_request.save()
