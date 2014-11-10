#coding:utf-8

from django.conf.urls import patterns, include, url
from blog import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^base/$', views.r_sidebar),
    (r'^blog/$', views.default),
    (r'^article/$', views.article_detail),
    (r'^article-list/$', views.article_list),
    (r'^themes/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': 'C:/myblog/themes/'}),
)
