from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def mainpage(request):
    return render(request, 'peteeting.html')

def petmap(request):
    return render(request, 'PET MAP.html')

def petchat(request):
    return render(request, 'PET CHAT.html')