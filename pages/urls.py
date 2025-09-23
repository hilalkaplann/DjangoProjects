from django.urls import path
from django import views

urlpatterns=[
    path('', views.home),
    path('anasayfa',views.home),
    path('iletisim', views.iletisim),
    path('hakkimizda', views.hakkimizda),

]