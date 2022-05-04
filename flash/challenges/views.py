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
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href = \"{month_path}\"> {capitalized_month}</a></li>"
    #side-by-side list items, now we wrap them in unordered list:
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
            return HttpResponseNotFound("<h1>Invalid month</h1>")
    else:
        redirect_month = months[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month]) #builds path that lloks like this: /challenge/<redirect_month>, which is why we use args = redirect_month as the second parameter
        return HttpResponseRedirect(redirect_path)
    

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound ('<h1>This month is not supported</h1>')
    
 