from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import Song, Album, Genre
from .forms import ArtistUpdateForm, SongCreateForm, AlbumCreateForm


POST_METHOD = 'POST'


def get_artist(username):
    """
    Returns the User model with the given username. Returns none if it doesn't exist.
    :param username: username of the desired User
    :return: User object
    """
    try:
        artist = get_user_model().objects.get(username=username)
        return artist
    except get_user_model().DoesNotExist:
        return None


class HomePageView(TemplateView):
    template_name = 'home.html'


def view_artist(request, username):
    artist = get_artist(username)
    if not artist:
        return Http404()
    template_name = 'artists/artist.html'
    context = {
        'artist': artist,
    }
    return render(request, template_name, context)


@login_required
def edit_artist(request, username):
    artist = get_artist(username)
    if not artist:
        return Http404('asdf')
    if request.user != artist:
        return Http404('asdf')

    form = ArtistUpdateForm(initial={
        'description': artist.description,
        'image': artist.image,
    })

    if request.method == POST_METHOD:
        form = ArtistUpdateForm(request.POST)
        if form.is_valid():
            artist.description = form.cleaned_data['description']
            artist.image = form.cleaned_data['image']
            artist.save()
            return redirect(artist)

    template_name = 'artists/edit_artist.html'
    context = {'form': form}
    return render(request, template_name, context)


def song_list(request):
    songs = Song.objects.all()
    template_name = 'music/song_list.html'
    context = {
        'songs': songs,
    }
    return render(request, template_name, context)


def view_song(request, song_slug):
    song = get_object_or_404(
        Song.objects.select_related('genre', 'album', 'artist'),
        slug=song_slug,
    )
    template_name = 'music/song.html'
    context = {
        'song': song,
    }
    return render(request, template_name, context)


@login_required
def create_song(request):
    form = SongCreateForm()

    if request.method == POST_METHOD:
        form = SongCreateForm(request.POST)
        if form.is_valid():
            new_song = Song(
                artist=request.user,
                title=form.cleaned_data['title'],
                description=form.cleaned_data['title'],
                youtube_id=form.cleaned_data['youtube_id'],
                genre=form.cleaned_data['genre'],
                album=form.cleaned_data['album'],
            )
            new_song.save()
            return redirect(new_song)

    template_name = 'music/new_song.html'
    context = {'form': form}
    return render(request, template_name, context)


@login_required
def edit_song(request, song_slug):
    song = get_object_or_404(
        Song.objects.select_related('genre', 'album', 'artist'),
        slug=song_slug
    )
    if song.artist != request.user:
        return Http404()

    youtube_link = 'https://www.youtube.com/watch?v=' + song.youtube_id
    form = SongCreateForm(initial={
        'title': song.title,
        'description': song.description,
        'youtube_link': youtube_link,
        'genre': song.genre,
        'album': song.album,
    })

    if request.method == POST_METHOD:
        form = SongCreateForm(request.POST)
        if form.is_valid():
            song.title = form.cleaned_data['title']
            song.description = form.cleaned_data['description']
            song.youtube_id = form.cleaned_data['youtube_id']
            song.genre = form.cleaned_data['genre']
            song.album = form.cleaned_data['album']
            song.save()
            return redirect(song)

    template_name = 'music/edit_song.html'
    context = {'form': form}
    return render(request, template_name, context)


@login_required
def view_album(request, album_slug):
    album = get_object_or_404(
        Album.objects.select_related('genre', 'artist'),
        slug=album_slug,
    )
    template_name = 'music/album.html'
    context = {
        'album': album,
    }
    return render(request, template_name, context)


@login_required
def create_album(request):
    pass