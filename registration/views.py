from django.shortcuts import render
from .models import Student
from django.contrib.auth.hashers import make_password,check_password
class Password:
    def encrypt(self,password):
        return make_password(password)

    def decrypt(self,enc_password,password):
       return check_password(enc_password,password)

def sign_in(request):        
    return render(request,'forms/sign-in.html')

def sign_up(request):
    if request.method == 'POST':
        obj = Password()
        s_name = request.POST['name']
        s_email = request.POST['email']
        s_password = request.POST['password']
        new_password = obj.encrypt(s_password)
        student = Student(s_name=s_name, s_email=s_email, s_password=new_password)

        try:
            student.save()
            return render(request,'forms/sign-in.html',{"message":"Successfully registered ! Please Sign in here !"})
        except:
            print("Unfortunately error occured. ")
    return render(request,'forms/sign-up.html')