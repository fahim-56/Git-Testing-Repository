from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def courses(request):
    return HttpResponse("This is course page in appname...")
def about(request):
    return HttpResponse("This is about page in appname...")
def home(request):
    return HttpResponse("This is Home page in appname...")