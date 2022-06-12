from django.db import models

from core.models import ModelBase
from movie.models import Movie
from room.models import Room
from show_date.models import ShowDate
from show_time.models import ShowTime


class ScheduleMovie(ModelBase):
    class Meta:
        db_table = "theater_schedule_movie"
        unique_together = ['room', 'show_date', 'show_time']

    movie = models.ForeignKey(Movie, related_name="schedule_movies", on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name="schedule_movies", on_delete=models.CASCADE)
    show_date = models.ForeignKey(ShowDate, related_name="schedule_movies", on_delete=models.CASCADE)
    show_time = models.ForeignKey(ShowTime, related_name="schedule_movies", on_delete=models.CASCADE)

    def __str__(self):
        return f"Movie: {self.movie} | Room: {self.room} " \
               f"| Date: {self.show_date} | Time: {self.show_time}"
