from django.conf.urls import patterns, include, url
from django.contrib import admin

from contacts import views as contact_views
from requests import views as requests_views
admin.autodiscover()

urlpatterns = patterns(
    '',
    # admin urls
    url(r'^admin/', include(admin.site.urls)),
    # contacts urls
    url(r'^$', contact_views.HomePageView.as_view(), name='home'),
    url(r'^last_requests/$',
        requests_views.RequestListView.as_view(),
        name='last_requests'
        ),
)
