"""
URL configuration for unit4_project_django_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    #Admin route
    path('admin/', admin.site.urls),

    #JWT Token endpoints
        #This is the URL Endpoint that will handle the generation of access and refresh tokens when user logins with valid credentials
            #The TokenObtainPairView.as_view() is the view that handles the POST request at the given URL Endpoint by sending user credentials and if valid, response is: 1.Access Token, 2.Refresh Token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    #This is the URL Endpoint that will handle the client sending the refresh token to the server after access token expires to RECEIVE a new access token, so that future requests remain authenticated
        #The TokenRefreshView.as_view() handles the POST request at this endpoint. It takes a valid refresh token and returns a new access token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #App routes
    path('', include('meat_department_api.urls')),
    path('', include('snacks_api.urls')),
    path('', include('beverage_department_api.urls')),
    path('', include('produce_api.urls')),
]
