from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = patterns(
    # admin urls
    url(r'^admin/', include(admin.site.urls)),
    #contacts urls
    url(r'^$', TemplateView.as_view(template_name='contacts/index.html'), name='home'),
)
