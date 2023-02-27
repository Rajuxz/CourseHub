
#-----[ Static File handling and URL Configuration goes here ]-----#
from django.urls import path
from .views import sign_in,sign_up
urlpatterns = [
    path('sign-in',sign_in,name="sign in"),
    path('sign-up', sign_up, name="sign up"),
]
