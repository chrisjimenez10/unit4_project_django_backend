from django.urls import path
from . import views

urlpatterns = [
    #URL Endpoints for Register and User Views (Register View: Create User (POST) - User View: List all users (GET) and display SINGLE user to view, edit or delete (GET, PUT, DELETE))
    path('api/register', views.RegisterView.as_view(), name='register'),
    path('api/users', views.UserListView.as_view(), name='user_list'),
    path('api/users/<int:pk>', views.UserDetailView.as_view(), name='user_detail')
]