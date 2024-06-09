from django.urls import path
from . import views

urlpatterns = [
    path('api/meats', views.MeatList.as_view(), name='meat_list'),
    path('api/meats/<int:pk>', views.MeatDetail.as_view(), name='meat_detail'),

    #URL Endpoint to user register view
    path('api/register', views.RegisterView.as_view(), name='register'),
    path('api/users', views.UserListView.as_view(), name='user_list'),
    path('api/users/<int:pk>', views.UserDetailView.as_view(), name='user_detail')
]