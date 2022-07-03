from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from rest_framework import (
    viewsets,
    generics,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from comment.models import Comment
from comment.serializers import CommentSerializer

@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                'movie_id',
                OpenApiTypes.INT,
                description='Movie ID',
            ),
        ]
    )
)
class ListCommentViewSet(viewsets.ViewSet,
                         generics.ListAPIView):
    queryset = Comment.objects.filter(is_deleted=False)
    serializer_class = CommentSerializer

    def get_queryset(self):
        comments = self.queryset
        movie_id = self.request.query_params.get("movie_id")
        if movie_id:
            comments = comments.filter(movie_id=movie_id).order_by('-created_at')
            return comments
        return comments


class CreateCommentViewSet(viewsets.ViewSet,
                           generics.CreateAPIView):
    queryset = Comment.objects.filter(is_deleted=False)
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class UpdateCommentViewSet(viewsets.ViewSet,
                           generics.UpdateAPIView):
    queryset = Comment.objects.filter(is_deleted=False)
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]