from django.urls import path
from . import views

urlpatterns = [
    path('api/snacks', views.SnacksList.as_view(), name='snacks_list'),
    path('api/snacks/<int:pk>', views.SnacksDetail.as_view(), name='snacks_detail'),
]