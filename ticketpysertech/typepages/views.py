from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "pages/home.html")

def newticket(request):
    return render(request, "pages/newticket.html")

def statusticket(request):
    return render(request, "pages/statusticket.html")
