from django.urls import path
# from app1.views import home
from app1 import views
# from . import views

urlpatterns = [
    path('',views.home)
]
