from django.shortcuts import redirect, render

from user.auth_form import LoginForm,SignupForm
from django.contrib .auth import authenticate, login
from django.contrib.auth.models import User


def login_view(request):
    if request.method=="POST":
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            username=login_form.cleaned_data['username']
            password=login_form.cleaned_data['password']
            user =authenticate(request,username=username,password=password)
            if user :
                login(request,user)
                return redirect('index')
            else:
                login_form.add_error('username','Wrong Username or Password')
                return render(request,'login.html',{ 'form':login_form})
    login_form=LoginForm()
    return render (request,'login.html',{'form':login_form})
# Create your views here.
def signup_view(request):
    if request.method=="POST":
            signup_form=SignupForm(request.POST)
            if signup_form.is_valid():
                username=signup_form.cleaned_data["username"]
                password=signup_form.cleaned_data["password"]
                email=signup_form.cleaned_data["email"] 
            user=User.objects.create_user(username=username,password=password,email=email)
            if user:

                user.save()
                return redirect('login')
            else:
                signup_form.add_error('username',"Username already exists")
                return render(request,"signup.html",{"form":signup_form}) #checking the uniqueness of the username and email 
            

    signup_form= SignupForm()  # An empty, unbound form
    return render(request,"signup.html",{"form":signup_form})


