from django.urls import path, include
from rest_framework.routers import DefaultRouter

from movie import views


router = DefaultRouter()
router.register('all', views.MovieViewSet, 'movie-list')
router.register('recommended_by_genre', views.ListRecommendedMovieViewSet, 'movie-recommend')

urlpatterns = [
    path('', include(router.urls)),
]