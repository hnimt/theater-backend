from django.urls import path, include
from rest_framework.routers import DefaultRouter

from comment import views

router = DefaultRouter()
router.register('', views.ListCommentViewSet, 'list')
router.register('create', views.CreateCommentViewSet, 'create')
router.register('update', views.UpdateCommentViewSet, 'update')

urlpatterns = [
    path('', include(router.urls)),
]