from django.urls import path
from . import views

urlPatterns = [
    path('beverages/', views.BeveragesList.as_view(), name='beverages_list'),
    path('beverages/<int:pk>/', views.BeverageDetail.as_view(), name='beverage_detail'),
]