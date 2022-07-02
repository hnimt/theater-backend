from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import ModelBase
from invoice.models import Invoice
from schedule_movie.models import ScheduleMovie
from seat.models import Seat


class ScheduleSeat(ModelBase):
    class Meta:
        db_table = "theater_schedule_seat"
        unique_together = ['schedule_movie', 'seat']

    schedule_movie = models.ForeignKey(ScheduleMovie,
                                       related_name="schedule_seats",
                                       on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat,
                             related_name="schedule_seats",
                             on_delete=models.CASCADE)
    invoice = models.ForeignKey(Invoice,
                                related_name="schedule_seats",
                                on_delete=models.SET_NULL,
                                null=True)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"Movie: {self.schedule_movie.movie} | " \
               f"Date: {self.schedule_movie.show_date} | " \
               f"Time: {self.schedule_movie.show_time} | " \
               f"Room: {self.schedule_movie.room} | " \
               f"Seat: {self.seat}"


@receiver(post_save, sender=ScheduleMovie)
def create_schedule_seat_by_schedule_movie(sender, instance, created, **kwargs):
    if created:
        seats = Seat.objects.filter(room=instance.room)
        for seat in seats:
            ScheduleSeat.objects.create(schedule_movie=instance,
                                        seat=seat, is_booked=False)

@receiver(post_save, sender=Seat)
def create_schedule_seat_by_seat(sender, instance, created, **kwargs):
    if created:
        schedule_movies = ScheduleMovie.objects.filter(room=instance.room).all()
        for schedule_movie in schedule_movies:
            ScheduleSeat.objects.create(schedule_movie=schedule_movie,
                                        seat=instance, is_booked=False)
