from django.urls import path
from . import views

urlpatterns = [
    path('api/beverages', views.BeveragesList.as_view(), name='beverages_list'),
    path('api/beverages/<int:pk>', views.BeverageDetail.as_view(), name='beverage_detail'),
]