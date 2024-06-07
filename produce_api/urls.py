from django.urls import path
from . import views

urlpatterns = [
    path('api/produce', views.ProduceList.as_view(), name='produce_list'),
    path('api/produce/<int:pk>', views.ProduceDetail.as_view(), name='produce_detail'),
]