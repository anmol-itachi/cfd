from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import person

def index(request):
    return render(request,'disater/index.html')

def person_status(request):
    all_persons=person.objects.all()
    context = {
        'all_persons':all_persons,
    }
    return render(request , 'disater/person_status.html',context)

def details(request,person_id):
    return HttpResponse("<h1>this has an id " + str(person_id) + "</h1>")
