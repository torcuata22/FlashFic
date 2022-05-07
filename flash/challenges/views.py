from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
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
    "december": None
    
}

# Create your views here.

def index(request): 
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html", {
        "months": months
    }) 

def challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        raise Http404
    else:
        redirect_month = months[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month]) #builds path that lloks like this: /challenge/<redirect_month>, which is why we use args = redirect_month as the second parameter
        return HttpResponseRedirect(redirect_path)
    

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render (request,"challenges/challenge.html", {
            "text": challenge_text , 
            "month_name": month   
        })
    except:
         raise Http404()