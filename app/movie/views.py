from datetime import datetime

from django.db.models import Q
from rest_framework import viewsets, generics
from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiTypes,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.paginator import MyPagination
from invoice.models import Invoice
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
            OpenApiParameter(
                'title',
                OpenApiTypes.STR,
                description='Title',
            ),
        ]
    )
)
class MovieViewSet(viewsets.ViewSet,
                   generics.ListAPIView,
                   generics.RetrieveAPIView):
    serializer_class = MovieSerializer
    pagination_class = MyPagination
    queryset = Movie.objects.filter(is_deleted=False)\
        .filter(Q(schedule_movies__show_date__value__gt=datetime.now().date()) |
                Q(schedule_movies__show_date__value=datetime.now().date(),
                  schedule_movies__show_time__value__gte=datetime.now().time()))\
        .order_by('-id').distinct()

    def get_queryset(self):
        genre_name = self.request.query_params.get('genre')
        actor_name = self.request.query_params.get('actor')
        director_name = self.request.query_params.get('director')
        title = self.request.query_params.get('title')

        if genre_name:
            self.queryset = self.queryset.filter(genres__name__icontains=genre_name)
        if actor_name:
            self.queryset = self.queryset.filter(actors__name__icontains=actor_name)
        if director_name:
            self.queryset = self.queryset.filter(directors__name__icontains=director_name)
        if title:
            self.queryset = self.queryset.filter(title__icontains=title)

        return self.queryset


class ListRecommendedMovieViewSet(viewsets.ViewSet,
                                  generics.ListAPIView):
    serializer_class = MovieSerializer
    pagination_class = MyPagination
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Movie.objects.filter(is_deleted=False) \
        .filter(Q(schedule_movies__show_date__value__gt=datetime.now().date()) |
                Q(schedule_movies__show_date__value=datetime.now().date(),
                  schedule_movies__show_time__value__gte=datetime.now().time())) \
        .order_by('-id').distinct()

    def list(self, request, *args, **kwargs):
        user = request.user
        invoices = Invoice.objects.filter(is_deleted=False, user=user) \
            .order_by('created_at')

        # If new user
        if len(invoices) == 0:
            return self.get_recommended_movies_for_new_or_anonymous_user(request)

        genre_count_dict = {}
        for invoice in invoices:
            schedule_seats = invoice.schedule_seats.all()
            if len(schedule_seats) > 0:
                schedule_movie = schedule_seats.all()[0].schedule_movie
                movie = schedule_movie.movie
                genres = movie.genres.all()
                for genre in genres:
                    if genre_count_dict.keys().__contains__(genre.name):
                        genre_count_dict[genre.name] = genre_count_dict[genre.name] + 1
                    else:
                        genre_count_dict[genre.name] = 1

            else:
                pass

        dict(sorted(genre_count_dict.items(), key=lambda x: x[1], reverse=True))
        movie_set = set([])
        for genre in genre_count_dict.keys():
            movies = self.queryset.filter(genres__name=genre)
            for movie in movies:
                if len(movie_set) < 6:
                    movie_set.add(movie)
                else:
                    break

        qs = self.paginator.paginate_queryset(list(movie_set), request)
        serializer = self.get_serializer(qs, many=True)
        return self.paginator.get_paginated_response(serializer.data)
