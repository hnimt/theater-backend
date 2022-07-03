from django.urls import path, include
from rest_framework.routers import DefaultRouter

from invoice import views

router = DefaultRouter()
router.register('', views.InvoiceViewSet, 'invoice-list')
router.register('update', views.UpdateInvoiceViewSet, 'invoice-update')

urlpatterns = [
    path('', include(router.urls)),
]