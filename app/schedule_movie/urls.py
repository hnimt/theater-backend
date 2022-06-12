from django.urls import path, include
from rest_framework.routers import DefaultRouter

from schedule_movie import views


router = DefaultRouter()
router.register('', views.ScheduleMovieViewSet, 'schedule-movie')

urlpatterns = [
    path('', include(router.urls)),
]