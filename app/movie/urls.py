from django.urls import path, include
from rest_framework.routers import DefaultRouter

from movie import views


router = DefaultRouter()
router.register('', views.MovieViewSet, 'movie')

urlpatterns = [
    path('', include(router.urls)),
]