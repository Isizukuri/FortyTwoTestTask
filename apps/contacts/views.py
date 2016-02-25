from django.views.generic.detail import DetailView

from .models import Contact


class HomePageView(DetailView):
    """CBV for homepage"""
    template_name = 'contacts/index.html'
    model = Contact

    def get_object(self, queryset=None):
        obj = Contact.objects.first()
        return obj
