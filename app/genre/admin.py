from django.contrib import admin

from genre.models import Genre


class GenreAdmin(admin.ModelAdmin):
    class Meta:
        model = Genre

    list_display = ['name']
    list_display_links = ['name']
    list_filter = ['name']


admin.site.register(Genre, GenreAdmin)
