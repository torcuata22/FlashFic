from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
monthly_challenges =  {
    "january": "Writing exercises for January",
    "february": "Writing exercise for Ferbuary",
    "march": "Writing exercise for March",
    "april": "Writing exercise for April",
    "may":"Writing exercise for Mary", 
    "june":"Writing exercise for June",
    "july":"Writing exercise for July",
    "august":"Writing exercise for August", 
    "september":"Writing exercise for September",
    "october":"Writing exercise for October",
    "november":"Writing exercise for November", 
    "december":"Writing exercise for December"
    
}

# Create your views here.

def index(request):
    return HttpResponse("A year of writing exercises")

def challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
            return HttpResponseNotFound("Invalid month")
    else:
        redirect_month = months[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month]) #builds path that lloks like this: /challenge/<redirect_month>, which is why we use args = redirect_month as the second parameter
        return HttpResponseRedirect(redirect_path)
    

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound ('This month is not supported')
    
    

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


