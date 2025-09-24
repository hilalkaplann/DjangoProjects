from django.urls import path
from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns=[
    path('list', views.kurslar),
    path('details',views.detail),
    path('programlama', views.programlama),
    path('mobil-uygulamalar', views.mobiluygulamalar),
    path('<str:category_name>', views.getCoursesByCategory),
    path('<int:category_id>', views.getCoursesByCategoryID),
    path('<kurs_adi>', views.detail),
    path('kategori/<int:category_id>', views.getCoursesByCategoryID),
    path('kategori/str:category_name>', views.getCoursesByCategory)
]