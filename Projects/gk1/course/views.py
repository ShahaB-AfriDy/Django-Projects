from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<h1 style="color: #FF5733; font-size: 36px; font-family: Arial, sans-serif; text-align: center;">About web page</h1>')

def Home(request):
    return HttpResponse('<h1 style="color: #FF5999; font-size: 36px; font-family: Arial, sans-serif; text-align: center;">Home page</h1>')

def About(request):
    return HttpResponse('<h1 style="color: #FF5999; font-size: 36px; font-family: Arial, sans-serif; text-align: center;">About page</h1>')