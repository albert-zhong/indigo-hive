from django.db import models


class Genre(models.Model):
    name = models.CharField()


class Artist(models.Model):
    name = models.CharField()


class Group(models.Model):
    pass


class Album(models.Model):
    title = models.CharField()
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)


class Song(models.Model):
    title = models.CharField()
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)
    album = models.ForeignKey(Album, null=True, on_delete=models.SET_NULL)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
