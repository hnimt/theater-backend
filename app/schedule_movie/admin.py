from django.contrib import admin

from schedule_movie.models import ScheduleMovie


class ScheduleMovieAdmin(admin.ModelAdmin):
    class Meta:
        model = ScheduleMovie

    list_display = ['id', 'movie', 'room', 'show_date', 'show_time']
    list_display_links = ['id', 'movie']

admin.site.register(ScheduleMovie, ScheduleMovieAdmin)
