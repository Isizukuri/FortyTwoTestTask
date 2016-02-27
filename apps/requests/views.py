import json

from django.views.generic import ListView
from .models import LastRequest
from django.http import HttpResponse


class JsonResponse(HttpResponse):
    """JSON response class for Django < 1.7"""
    def __init__(self, content, content_type='application/json', status=None):
        super(JsonResponse, self).__init__(
            content=json.dumps(content),
            status=status,
            content_type=content_type,
        )


class RequestListView(ListView):
    """View that displays last 10 requests"""
    template_name = "requests/last_requests.html"
    model = LastRequest

    def get_queryset(self):
        queryset = super(RequestListView, self).get_queryset()
        queryset = queryset.order_by('-timestamp')[:10]
        return queryset

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            if self.get_queryset():
                response = []
                for item in self.get_queryset():
                    response.append({
                        'pk': item.pk,
                        'url': item.url,
                        'method': item.method,
                        'timestamp': str(item.timestamp)
                    })
                response = JsonResponse(response)
            else:
                response = {'error': 'There are no requests at all.'}
                response = JsonResponse(response)
        else:
            response = super(RequestListView, self).get(
                self, request, *args, **kwargs)
            return response
        return response
