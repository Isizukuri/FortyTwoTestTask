from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from apps.contacts import views as contact_views
admin.autodiscover()

urlpatterns = patterns(
    '',
    # admin urls
    url(r'^admin/', include(admin.site.urls)),
    # contacts urls
    url(r'^$', contact_views.HomePageView.as_view(), name='home'),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
