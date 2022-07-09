from django.contrib import admin

from invoice.models import Invoice


class InvoiceAdmin(admin.ModelAdmin):
    class Meta:
        model = Invoice

    readonly_fields = ['id', 'user', 'tax', 'total']
    list_display = ['id', 'user', 'get_movie', 'get_room', 'get_show_date', 'get_show_time', 'is_pay']
    list_display_links = ['id', 'user']
    search_fields = ['id' ,'user__email']
    list_filter = ['is_pay']

    @admin.display(description='movie')
    def get_movie(self, obj):
        schedule_seats = obj.schedule_seats.all()
        if len(schedule_seats) > 0:
            return schedule_seats[0].schedule_movie.movie.title
        else:
            return '<Blank>'

    @admin.display(description='room')
    def get_room(self, obj):
        schedule_seats = obj.schedule_seats.all()
        if len(schedule_seats) > 0:
            return schedule_seats[0].schedule_movie.room.name
        else:
            return '<Blank>'

    @admin.display(description='show date')
    def get_show_date(self, obj):
        schedule_seats = obj.schedule_seats.all()
        if len(schedule_seats) > 0:
            return schedule_seats[0].schedule_movie.show_date.value
        else:
            return '<Blank>'

    @admin.display(description='show time')
    def get_show_time(self, obj):
        schedule_seats = obj.schedule_seats.all()
        if len(schedule_seats) > 0:
            return schedule_seats[0].schedule_movie.show_time.value
        else:
            return '<Blank>'


admin.site.register(Invoice, InvoiceAdmin)
