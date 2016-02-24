from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.contacts import views as contact_views
admin.autodiscover()

urlpatterns = patterns(
    # admin urls
    url(r'^admin/', include(admin.site.urls)),
    # contacts urls
    url(r'^$', contact_views.HomePageView.as_view(), name='home'),
)
