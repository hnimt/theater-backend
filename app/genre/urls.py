from django.urls import path, include
from rest_framework.routers import DefaultRouter

from genre import views


router = DefaultRouter()
router.register('', views.GenreViewSet, 'genre')

urlpatterns = [
    path('', include(router.urls)),
]