from django.contrib import admin

from .models import Song, Album, Genre


admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Genre)
