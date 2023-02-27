from django.shortcuts import render

def sign_in(request):
    return render(request,'forms/sign-in.html')

def sign_up(request):
    return render(request,'forms/sign-up.html')