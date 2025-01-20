from django.http import HttpResponse
def homepage(request):
    return HttpResponse("Reached at Home Page, Alhamdulillah...")
def contact(request):
    return HttpResponse("Reached at Connect Page, Alhamdulillah...")