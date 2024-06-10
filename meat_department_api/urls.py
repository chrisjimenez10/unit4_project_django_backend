from django.urls import path
from . import views

urlpatterns = [
    #URL Endpoints for Meats Views
    path('api/meats', views.MeatList.as_view(), name='meat_list'),
    path('api/meats/<int:pk>', views.MeatDetail.as_view(), name='meat_detail'),
]