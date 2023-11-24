from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def mainpage(request):
    return render(request, 'peteeting.html')

def petmap(request):
    return render(request, 'map.html')

def petchat(request):
    return render(request, 'chat.html')

def community(request):
    return render(request, 'community.html')

def mainlogin(request):
    return render(request, 'login.html')

def homelogin(request):
    return render(request, 'h_login.html')

def place(request):
    return render(request, 'place.html')

