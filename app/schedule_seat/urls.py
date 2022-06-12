from django.urls import path, include
from rest_framework.routers import DefaultRouter

from schedule_seat import views


router = DefaultRouter()
router.register('', views.ScheduleSeatView, 'schedule-seat')

urlpatterns = [
    path('', include(router.urls)),
]