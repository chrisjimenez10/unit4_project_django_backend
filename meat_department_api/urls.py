from django.urls import path
from . import views

urlpatterns = [
    path('api/meats', views.MeatList.as_view(), name='meat_list'),
    path('api/meats/<int:pk>', views.MeatDetail.as_view(), name='meat_detail')
]