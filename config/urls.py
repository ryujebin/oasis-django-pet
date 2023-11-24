"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
import pet.views

urlpatterns = [
    path('', pet.views.mainpage, name='mainpage'), #포트 연결 시 pet/views.py의 mainpage 함수에 해당하는 부분을 기본url로 지정
    path('map.html', pet.views.petmap, name='petmap'),
    path('chat.html', pet.views.petchat, name='petchat'),
    path('place.html', pet.views.place, name='place'),
    path('community.html', pet.views.community, name='community'),
    path('h_login.html', pet.views.homelogin, name='homelogin'),
    path('login.html', pet.views.mainlogin, name='mainlogin'),
    
    
]
