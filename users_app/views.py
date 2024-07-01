from django.shortcuts import render, redirect
from .forms import CustomRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.http import HttpResponse


# Create your views here.

def register(request):
    
    if request.method=="POST":
        register_form=CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,("New User Account Created"))
            return redirect('register')
        
    else:
        register_form= CustomRegisterForm() 
    return render(request,'register.html', {'registerr_form':register_form})



def logout_view(request):
    logout(request)
    return redirect('login')
    

    
    
    
    
