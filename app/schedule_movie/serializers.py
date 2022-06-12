from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from movie.serializers import MovieSerializer
from schedule_movie.models import ScheduleMovie


class ScheduleMovieSerializer(serializers.ModelSerializer):
    room = SerializerMethodField()
    show_date = SerializerMethodField()
    show_time = SerializerMethodField()
    movie = MovieSerializer(read_only=True)

    def get_room(self, obj):
        return obj.room.name

    def get_show_date(self, obj):
        return obj.show_date.value

    def get_show_time(self, obj):
        return obj.show_time.value

    class Meta:
        model = ScheduleMovie
        fields = ['id', 'movie', 'room', 'show_date', 'show_time']
