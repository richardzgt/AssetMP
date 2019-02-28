from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from AssetMP.views import *
from vms.views import *
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'AssetMP.views.dashboard', name='dashboard'),
    url(r'^cabinet/', Cabinet.as_view(), name='cabinet'),
    url(r'^assets/', Assets.as_view(), name='assets'),
    url(r'^detail/', AssetDetail.as_view(), name='asset_detail'),
    url(r'^vmscreate/', VmsCreate.as_view(), name='vms_create'),
    url(r'^getCorp/', getCorp.as_view(), name='getCorp'),
    url(r'^test/', test.as_view(), name='test'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG is False:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT}),
        )