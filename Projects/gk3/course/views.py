
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Student_Course(request):
    return HttpResponse('<h1 style="color: #FF5999; font-size: 36px; font-family: Arial, sans-serif; text-align: center;">Student Course</h1>')

def Student_Course_Detail(request):
    return HttpResponse('<h1 style="color: #FF5999; font-size: 36px; font-family: Arial, sans-serif; text-align: center;">Student Course Detail</h1>')
