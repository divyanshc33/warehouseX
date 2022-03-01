from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is home page")
    
def location(request):
    return HttpResponse("this is services page") 
    
def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page")
    
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date= datetime.today())
        contact.save()
        messages.success(request, 'Message sent successfully!!!')

    return render(request, 'contact.html')
    # return HttpResponse("this is contact page")

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def logout(request):
    return render(request, 'index.html')