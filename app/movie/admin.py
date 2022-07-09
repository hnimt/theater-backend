from django.contrib import admin

from movie.models import Movie


class MovieAdmin(admin.ModelAdmin):
    class Meta:
        model = Movie

    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']

admin.site.register(Movie, MovieAdmin)
