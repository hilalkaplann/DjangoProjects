from django.urls import path
from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns=[
    path('list', views.kurslar),
    path('details',views.detail),
    path('programlama', views.programlama),
    path('mobil-uygulamalar', views.mobiluygulamalar),
    path('<category>', views.getCoursesByCategory)
]