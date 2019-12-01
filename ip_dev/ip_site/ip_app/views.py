from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Person

def index(request):
    return render(request, "index.html")

def create(request):
    if request.method == "POST":
        tom = Person()
        tom.name =  request.POST.get('name')
        tom.title = request.POST.get('title')
        tom.inn = request.POST.get('inn')
        tom.telefon = request.POST.get('telefon')
        tom.pred = request.POST.get('pred')
        tom.postav = request.POST.get('postav')
        tom.gruz = request.POST.get('gruz')
        tom.save()
    return HttpResponseRedirect("/")

def auth(request):
    return render(request,'registrashion.html')

def ls(request):
    return render(request,'ls.html')

def vxod(request):
    people = Person.objects.all()
    