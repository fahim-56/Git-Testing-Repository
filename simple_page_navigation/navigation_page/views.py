from django.shortcuts import render

# Create your views here.
def home(request):
    pass

def about(request):
    return render(request,'navigation_page/about.html')
    

def contact(request):
    return render(request,'navigation_page/contact.html')