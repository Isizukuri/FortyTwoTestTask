from django.views.generic import ListView
from .models import LastRequest


class RequestListView(ListView):
    """View that displays last 10 requests"""
    template_name = "requests/last_requests.html"
    model = LastRequest

    def get_queryset(self):
        queryset = super(RequestListView, self).get_queryset()
        queryset = queryset.order_by('-timestamp')[:10]
        return queryset

