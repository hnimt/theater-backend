from rest_framework import viewsets, generics
from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiTypes,
)

from core.paginator import BasePagination
from movie.models import Movie
from movie.serializers import MovieSerializer


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                'genre',
                OpenApiTypes.STR,
                description='Genre name',
            ),
            OpenApiParameter(
                'actor',
                OpenApiTypes.STR,
                description='Actor name',
            ),
            OpenApiParameter(
                'director',
                OpenApiTypes.STR,
                description='Director name',
            ),
        ]
    )
)
class MovieViewSet(viewsets.ViewSet,
                   generics.ListAPIView,
                   generics.RetrieveAPIView):
    serializer_class = MovieSerializer
    pagination_class = BasePagination
    queryset = Movie.objects.filter(is_deleted=False)

    def get_queryset(self):
        genre_name = self.request.query_params.get('genre')
        actor_name = self.request.query_params.get('actor')
        director_name = self.request.query_params.get('director')

        if genre_name:
            self.queryset = self.queryset.filter(genres__name__icontains=genre_name)
        if actor_name:
            self.queryset = self.queryset.filter(actors__name__icontains=actor_name)
        if director_name:
            self.queryset = self.queryset.filter(directors__name__icontains=director_name)

        return self.queryset.order_by('-id').distinct()
