from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.GetUpdateUserView.as_view(), name='me'),
    path('change_password/<int:pk>/', views.ChangePasswordView.as_view(), name='change_password'),
]
