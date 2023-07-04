# We will create functions which will fire when user visits certail url
from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return render(request, 'Home.html')
    # return HttpResponse('This is the Home page')

def About(request):
    return render(request, 'About.html')
    # return HttpResponse('This is about page')