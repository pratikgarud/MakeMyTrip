from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login
from . forms import RegisterForm

# Create your views here.
def Login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.info(request,'Now you are login.')
            return redirect('index')
        else:
            messages.error(request,'Invalid username and password.')
    form = AuthenticationForm()
    return render(request=request,template_name='Login.html',context={'form':form})

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'Your account has been created.Now login Successfully..')
            return redirect('Login')
        messages.info(request,'Unsuccessful Registration,Invalid information.')
    else:
        form = RegisterForm()
    return render(request,'register.html',{'form':form})

def Logout(request):
    auth.logout(request)
    return redirect('index')