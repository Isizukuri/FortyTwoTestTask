from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    # admin urls
    url(r'^admin/', include(admin.site.urls)),
    # contacts urls
)
