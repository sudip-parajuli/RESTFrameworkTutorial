from django.contrib import admin

from movie_app.models import Movie, StreamPlatform

# Register your models here.
admin.site.register(Movie)

"""registered new updated models StreamPlatform and WatchList """
admin.site.register(['StreamPlatform','WatchList'])