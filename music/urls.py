# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from music_web import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search_index/$', views.index, name = 'search_index'),  # 页面
    url(r'^details_html/$', views.details_html, name = 'details_html'),  # 详情页面
    url(r'^search_music/$', views.music_id, name = 'music_id'), # 搜索id API
    url(r'^music_uid_data/$',views.music_uid_data, name = 'music_uid_data'), # 结果集
]
