from django.conf.urls import url
from horse_show import views
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    # enable the admin and admin docs
    url(r'^admin/', admin.site.urls),

    # The main index
    url(r'^$', lambda r: HttpResponseRedirect('/HSPro/')),
    url(r'^HSPro/$', views.index),
    url(r'^HSPro/(?P<show_id>[0-9]+)/$', views.list_classes, name='list-classes'),
    url(r'^HSPro/(?P<show_id>[0-9]+)/classes/(?P<class_id>[0-9]+)/print/$', views.print_class),
    url(r'^HSPro/(?P<show_id>[0-9]+)/classes/(?P<class_id>[0-9]+)/print_split/$', views.print_split_class),
    url(r'^HSPro/(?P<show_id>[0-9]+)/riders/(?P<ridernum>[0-9a-zA-Z]*)/welcome/$', views.print_rider_sheet),

    url(r'^HSPro/shows/json/$', views.api_get_shows),
    url(r'^HSPro/shows/(?P<show_id>[0-9]+)/json/$', views.api_show),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
