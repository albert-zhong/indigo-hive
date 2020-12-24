from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from .utils import random_string


ALBUM_SLUG_MAX_LEN = 63
SONG_SLUG_MAX_LEN = 63
RANDOM_STRING_LEN = 10


class Genre(models.Model):
    name = models.CharField(max_length=31)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=ALBUM_SLUG_MAX_LEN, unique=True)
    description = models.CharField(max_length=2047, null=True)
    image = models.URLField(max_length=1023, null=True)
    genre = models.ForeignKey(
        Genre,
        null=True,
        on_delete=models.SET_NULL,
        related_name='albums',
    )
    artist = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='albums',
    )

    def save(self, *args, **kwargs):
        self.slug = Album.unique_slugify(self.title)
        super(Album, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_album', kwargs={'album_slug': self.slug})

    @staticmethod
    def unique_slugify(title):
        """
        Returns a unique slug for an Album based on its title.
        :param title: the title of the Album
        :return: a unique slug for the Album
        """
        slug_title = slugify(title)
        if len(slug_title) > ALBUM_SLUG_MAX_LEN - RANDOM_STRING_LEN:
            slug_title = slug_title[:ALBUM_SLUG_MAX_LEN - RANDOM_STRING_LEN]
        base_slug_title = slug_title
        while Album.objects.filter(slug=slug_title).exists():
            slug_title = base_slug_title + random_string(size=RANDOM_STRING_LEN)
        return slug_title


class Song(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=SONG_SLUG_MAX_LEN, unique=True)
    description = models.CharField(max_length=2047, null=True)
    youtube_id = models.CharField(max_length=11)
    genre = models.ForeignKey(
        Genre,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    album = models.ForeignKey(
        Album,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='songs',
    )
    artist = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='songs',
    )

    def save(self, *args, **kwargs):
        self.slug = Song.unique_slugify(self.title)
        super(Song, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_song', kwargs={'song_slug': self.slug})

    @staticmethod
    def unique_slugify(title):
        """
        Returns a unique slug for an Song based on its title.
        :param title: the title of the Song
        :return: a unique slug for the Song
        """
        slug_title = slugify(title)
        if len(slug_title) > SONG_SLUG_MAX_LEN - RANDOM_STRING_LEN:
            slug_title = slug_title[:SONG_SLUG_MAX_LEN - RANDOM_STRING_LEN]
        base_slug_title = slug_title
        while Song.objects.filter(slug=slug_title).exists():
            slug_title = base_slug_title + random_string(size=RANDOM_STRING_LEN)
        return slug_title
