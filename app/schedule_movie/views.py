from datetime import datetime
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from rest_framework import viewsets, status, generics
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from movie.serializers import MovieScheduleSerializer
from schedule_movie.models import ScheduleMovie
from schedule_movie.serializers import ScheduleMovieSerializer


@extend_schema_view(
    get_movie_scheduler=extend_schema(
        parameters=[
            OpenApiParameter(
                'movie_id',
                OpenApiTypes.INT,
                description='movie id',
            ),
        ]
    )
)
class ScheduleMovieViewSet(viewsets.ViewSet,
                           generics.CreateAPIView,
                           generics.UpdateAPIView):
    serializer_class = ScheduleMovieSerializer
    queryset = ScheduleMovie.objects.filter(is_deleted=False)

    @action(methods=['get'], detail=False, url_path='movie-scheduler')
    def get_movie_scheduler(self, request):
        if self.request.query_params.get('movie_id'):
            movie_id = self.request.query_params.get('movie_id')
            schedule_movies = self.queryset\
                .filter(movie__id=movie_id,
                        show_date__value__gte=datetime.now().date())\
                .order_by('show_date__value', 'show_time__value')

            if len(schedule_movies) > 0:
                movie = schedule_movies[0].movie
                schedule_movies_serializer = ScheduleMovieSerializer(schedule_movies,
                context={"request": request},
                many = True).data

                schedule_dict = {}
                for i in schedule_movies_serializer:
                    schedule_dict.setdefault(str(i['show_date']), []).append(
                        {'id': i['id'], 'show_time': str(i['show_time'])})
                schedule_list = [{k: v} for k, v in schedule_dict.items()]
                res = MovieScheduleSerializer(movie, context={"request": request, 'show_dates': schedule_list}).data

                return Response(res, status=status.HTTP_200_OK)

            raise NotFound("Not contain any movie")

        raise NotFound("Not contain movie param")
