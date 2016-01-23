from blog import views
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', views.index), #默认显示分页
    url(r'^view/(.+?)/',views.look), #http//host:post/blog/view/*/ 显示页面
)
