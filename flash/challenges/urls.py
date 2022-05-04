from django.urls import path

from . import views
urlpatterns = [
    path("", views.index),
    path("<int:month>", views.challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
    
    
]
