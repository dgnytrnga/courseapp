from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('anasayfa')

def kurslar(request):
    return HttpResponse("Kurs Listesi")

def hakkimizda(request):
    return HttpResponse("hakkımızda sayfası")

def iletisim(request):
    return HttpResponse("İletişim Sayfası")
# Create your views here.
