from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

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
    return render(request, 'contact.html')
    # return HttpResponse("this is contact page")