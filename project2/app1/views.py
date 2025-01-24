from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("I am at home...!")
    return render(request,'app1/page.html')