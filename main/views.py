import re
from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import redirect

def home(request):
    return render(request, "main/index.html")

def services(request):
    return render(request, "main/services.html")    

def about(request):
    return render(request, "main/about.html")

def contact(request):
    return render(request, "main/contact.html")
    
