from django.urls import path

from . import views
urlpatterns = [
    path('', views.index),
    path("<int:month>", views.challenge_by_number),
    path("<str:month>", views.monthly_challenge)
    # path('january', views.first),
    # path('february', views.second),
    # path('march', views.third),
    # path('april', views.fourth),
    # path('may', views.fifth),
    # path('june', views.sixth),
    # path('july', views.seventh),
    # path('august', views.eighth),
    # path('september', views.ninth),
    #  path('october', views.tenth),
    # path('november', views.eleventh),
    # path('december', views.twelfth)
]
