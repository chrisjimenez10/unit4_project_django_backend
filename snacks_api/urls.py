from django.urls import path
from . import views

urlpatterns = [
    path('api/contacts', views.SnacksList.as_view(), name='snacks_list'),
    path('api/contacts/<int:pk>', views.SnacksDetail.as_view(), name='snacks_detail'),
]