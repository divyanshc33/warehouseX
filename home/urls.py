from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",  views.index, name='home'),
    path("location",  views.location, name='location'),
    path("contact",  views.contact, name='contact'),
    path("about",  views.about, name='about'),
    path("contact",  views.contact, name='contact')
]
