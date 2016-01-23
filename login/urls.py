from django.conf.urls import patterns, url
from login import views as login


urlpatterns = patterns('',
    url(r'^$', login.login),
    url(r'^login/$', login.login),
    url(r'^regist/$', login.regist),
    url(r'^index/$', login.index),
    url(r'^logout/$', login.logout),
)
