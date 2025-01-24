from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    # Context means pass data backend to fontend
    d ={'author':'Md Fahim Chowdhury' ,'age': 23,'list':[1,2,3],
        'courses': [{
            'id': 25,
            'name': 'kawshik',
            'dept': 'CSE'
        },
        {
            'id': 26,
            'name': 'Tonmoy',
            'dept': 'CSE'
        },
        {
            'id': 27,
            'name': 'Fahim',
            'dept': 'CSE'
        }],
        'Str_list':['Md',"Fahim","Chowdhury"],
        'today': datetime.datetime.now(),
        'value' : 27,
        }
    return render(request,'home.html',d)