from django.urls import path
from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns=[
    path('', views.home),
    path('anasayfa',views.home),
    path('kurslar', views.kurslar),
]