from django.contrib import admin

from schedule_seat.models import ScheduleSeat


class ScheduleSeatAdmin(admin.ModelAdmin):
    class Meta:
        model = ScheduleSeat

    list_display = ['id', 'get_movie', 'get_show_date', 'get_show_time', 'get_room', 'seat']
    list_display_links = ['id', 'get_movie']

    @admin.display(description='movie')
    def get_movie(self, obj):
        return obj.schedule_movie.movie

    @admin.display(description='show_date')
    def get_show_date(self, obj):
        return obj.schedule_movie.show_date

    @admin.display(description='show_time')
    def get_show_time(self, obj):
        return obj.schedule_movie.show_time

    @admin.display(description='room')
    def get_room(self, obj):
        return obj.schedule_movie.room


admin.site.register(ScheduleSeat, ScheduleSeatAdmin)
