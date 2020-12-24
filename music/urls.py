from django.urls import path

from .views import (
    song_list,
    view_song,
    edit_song,
    create_song,
    view_album,
    create_album,
    view_artist,
    edit_artist,
)

urlpatterns = [
    path('', song_list, name='home'),
    path('artist/<str:username>', view_artist, name='view_artist'),
    path('artist/<str:username>/edit', edit_artist, name='edit_artist'),
    path('song/view/<slug:song_slug>', view_song, name='view_song'),
    path('song/edit/<slug:song_slug>', edit_song, name='edit_song'),
    path('song/create', create_song, name='create_song'),
    path('album/view/<slug:album_slug>', view_album, name='view_album'),
    path('album/create', create_album, name='create_album'),
]
