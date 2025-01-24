from django.http import HttpResponse

def home(request):
    return HttpResponse("I am at home!")