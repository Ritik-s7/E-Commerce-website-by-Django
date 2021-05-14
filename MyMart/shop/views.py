from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"shop/index.html")

def about(request):
    return HttpResponse("You're at About")

def contact(request):
    return HttpResponse("You're at Contact Us")

def tracker(request):
    return HttpResponse("You're at Tracker")

def search(request):
    return HttpResponse("You're at Search")

def productView(request):
    return HttpResponse("You're at Product View")

def checkOut(request):
    return HttpResponse("You're at Check out")