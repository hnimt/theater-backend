from rest_framework import viewsets, mixins

from genre.models import Genre
from genre.serializers import GenreSerializer


class GenreViewSet(viewsets.GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin):
    queryset = Genre.objects.filter(is_deleted=False)
    serializer_class = GenreSerializer
