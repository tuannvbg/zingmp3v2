from django.conf.urls import url
from . import views
from . import admin

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^zmp3-song/(?P<song_xml>.+)$', views.zmp3_song, name='zmp3_song'),
    url(r'^list-song$', views.list_song, name='list_song'),
    url(r'^song/(?P<song_slug>.+)-(?P<song_id>.+)$', views.play_song, name='play_song'),
    url(r'^favor-song$', views.favor_song, name='favor_song'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^song/(?P<username>.+)', views.user_song, name='user_song'),
    url(r'^create-lyrics/select-song$', admin.select_song, name='select_song'),
    url(r'^create-lyrics/(?P<song_xml>.+)$', admin.create_lyrics, name='create_lyrics'),
    url(r'^update-lyrics/(?P<song_slug>.+)-(?P<song_id>.+)$', admin.update_lyrics, name='update_lyrics'),
]

urlpatterns += [
    url(r'^biadmin$', admin.index, name='admin_index'),
    url(r'^biadmin/list-song$', admin.list_song, name='admin_list_song'),
    url(r'^biadmin/charts$', admin.chart, name='admin_chart'),
]

urlpatterns += [
    url(r'^ajax/subtitles/(?P<song_id>\d*)$', admin.ajax_subtitles, name='ajax_subtitles'),
    url(r'^ajax/increment-view/(?P<song_id>\d*)$', views.ajax_increment_view, name='ajax_increment_view'),
    url(r'^ajax/favor/(?P<song_id>\d*)$', views.ajax_favor, name='ajax_favor'),
    url(r'^ajax/search$', views.ajax_search_song, name='ajax_search_song'),
    url(r'^ajax/songs/(?P<song_id>\d*)$', admin.ajax_song, name='ajax_song'),
    url(r'^ajax/get-zmp3id$', admin.get_zmp3id, name='get_zmp3id'),
    url(r'^ajax/get-view-everyday$', admin.get_song_tracking, name='get_view_everyday'),
]
