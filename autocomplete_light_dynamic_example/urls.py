import autocomplete_light
from django.conf.urls import patterns, include, url
from django.contrib import admin

from example.views import form_test

autocomplete_light.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', form_test),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
)
