from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse('anasayfa')

def details(request):
    return HttpResponse('kurs detay listesi')
def programlama(request):
    return HttpResponse('programlama kurs listesi')


def mobiluygulamalar(request):
    return HttpResponse('mobil uygulamalar kurs listesi')
def getCoursesByCategory(request, category):
    return HttpResponse('kategoriye göre kurs listesi')