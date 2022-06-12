from django.contrib import admin

from seat.models import Seat


class SeatAdmin(admin.ModelAdmin):
    class Meta:
        model = Seat

    list_display = ['id', '__str__', 'room', 'type']
    list_filter = ['room__name']
    search_fields = ['room__name']

admin.site.register(Seat, SeatAdmin)
