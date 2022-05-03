from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def index(request):
    return HttpResponse("A year of writing exercises")

def challenge_by_number(request, month):
    return HttpResponse(month)
    

def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = 'Writing exercise for January'
    elif month == 'february':
        challenge_text='Writing exercise for February'
    elif month == 'march':
        challenge_text='Writing exercise for March'
    else:
        return HttpResponseNotFound ('This month is not supported')
    
    return HttpResponse(challenge_text)
    

# def first(request):
#     return HttpResponse("Writing exercise for January!")

# def second(request):
#     return HttpResponse("Writing exercise for February!")

# def third(request):
#     return HttpResponse("Writing exercise for March!")

# def fourth(request):
#     return HttpResponse("Writing exercise for April!")

# def fifth(request):
#     return HttpResponse("Writing exercise for May!")

# def sixth(request):
#     return HttpResponse("Writing exercise for June!")

# def seventh(request):
#     return HttpResponse("Writing exercise for July!")

# def eighth (request):
#     return HttpResponse("Writing exercise for August!")

# def ninth(request):
#     return HttpResponse("Writing exercise for September!")

# def tenth(request):
#     return HttpResponse("Writing exercise for October!")

# def eleventh(request):
#     return HttpResponse("Writing exercise for November!")

# def twelfth(request):
#     return HttpResponse("Writing exercise for December!")


