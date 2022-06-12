from rest_framework import serializers

from actor.serializers import ActorSerializer
from director.serializers import DirectorSerializer
from genre.serializers import GenreSerializer
from movie.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    directors = DirectorSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'image', 'genres', 'directors', 'actors', 'created_at', 'updated_at']


class MovieScheduleSerializer(MovieSerializer):
    show_dates = serializers.SerializerMethodField()

    def get_show_dates(self, obj):
        return self.context['show_dates']

    class Meta(MovieSerializer.Meta):
        fields = MovieSerializer.Meta.fields + ['show_dates']
    