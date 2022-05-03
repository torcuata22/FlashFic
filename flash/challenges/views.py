from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("A year of writing exercises")

def first(request):
    return HttpResponse("Writing exercise for January!")

def second(request):
    return HttpResponse("Writing exercise for February!")

def third(request):
    return HttpResponse("Writing exercise for March!")

def fourth(request):
    return HttpResponse("Writing exercise for April!")

def fifth(request):
    return HttpResponse("Writing exercise for May!")

def sixth(request):
    return HttpResponse("Writing exercise for June!")

def seventh(request):
    return HttpResponse("Writing exercise for July!")

def eighth(request):
    return HttpResponse("Writing exercise for August!")

def ninth(request):
    return HttpResponse("Writing exercise for September!")

def tenth(request):
    return HttpResponse("Writing exercise for October!")

def eleventh(request):
    return HttpResponse("Writing exercise for November!")

def twelfth(request):
    return HttpResponse("Writing exercise for December!")


