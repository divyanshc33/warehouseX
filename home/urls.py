from django.contrib import admin
from django.urls import path
from home import views

#Adimn
admin.site.site_header = "WarehouseX Admin"
admin.site.site_title = "WarehouseX Admin Portal"
admin.site.index_title = "Welcome to WarehouseX Portal"

urlpatterns = [
    path("",  views.index, name = "home"),
    path("location",  views.location, name = "location"),
    path("contact",  views.contact, name = "contact"),
    path("about",  views.about, name = "about"),
    path("contact",  views.contact, name = "contact"),
    path("login",  views.login, name = "login"),
    path("signup", views.signup, name = "signup"),
    path("logout",  views.logout, name = "logout")
]