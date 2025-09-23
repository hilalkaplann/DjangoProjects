from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse('anasayfa')

def detail(request):
    return HttpResponse('kurs detay listesi')

def programlama(request):
    return HttpResponse('programlama kurs listesi')


def mobiluygulamalar(request):
    return HttpResponse('mobil uygulamalar kurs listesi')

def getCoursesByCategory(request, category):
    if(category=="programlama"):
        text="programlama kategorisine ait kurslar"
    elif(category=="web-gelistirme"):
        text="web geliştirme kategorisi"
    else:
        text="yanlış kategori"
    return HttpResponse(text)  
#return HttpResponse(f'{category} kategorisindeki kurs listesi')

def getCoursesByCategoryID(request, category_id):
    return HttpResponse(category_id)
    
def kurslar(request):
    return HttpResponse('kurs listesi')