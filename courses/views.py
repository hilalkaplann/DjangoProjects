from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


data = {
    "programlama":"programlama katagorisine ait kurslar"
}
# Create your views here.
def home(request):
    return HttpResponse('anasayfa')

def index(request):
    return render(request, 'courses/index.html')

def details(request):
    return HttpResponse(f"{kurs_adi} detay sayfası")

def programlama(request):
    return HttpResponse('programlama kurs listesi')


def mobiluygulamalar(request):
    return HttpResponse('mobil uygulamalar kurs listesi')

def getCoursesByCategory(request, category_name):
    try:
        category_text=data[category_name]
    
    except:
        return HttpResponseNotFound("yanlış kategori seçimi")  
#return HttpResponse(f'{category} kategorisindeki kurs listesi')

def getCoursesByCategoryID(request, category_id):
    category_list=list(data.keys())
    if(category_id>len(category_list)):
        return HttpResponseNotFound("yanlış kategori seçimi")
    category_name=category_list(category_id - 1)
    redirect_url=reverse('courses_by_category', args=[category_name])
    return HttpResponseRedirect(redirect_url)
    
def kurslar(request):
    list_items=""
    category_list = list(data.keys())

    for category in category_list:
        redirect_url=reverse('courses_by_category', args=[category])    
        list_items += f"<li><a href='{redirect_url}'> {category}</a></li>"
    html=f"<h1>kurs listesi</h1><ul>{list_items}</ul>"
    return HttpResponse(html)
