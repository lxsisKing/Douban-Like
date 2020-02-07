from django.contrib import admin

# Register your models here.

from . import models


class MovieDataAdmin(admin.ModelAdmin):
    list_display = ['movie_name', 'movie_orig_name', 'movie_rate', 'movie_type']


admin.site.register(models.MovieData2019, MovieDataAdmin)
admin.site.register(models.MovieData2018, MovieDataAdmin)
