from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Student_Attendence(request):
    return HttpResponse('<h1 style="color: #FF5999; font-size: 36px; font-family: Arial, sans-serif; text-align: center;">Student Attendence</h1>')

def Student_Record(request):
    return HttpResponse('<h1 style="color: #FF5999; font-size: 36px; font-family: Arial, sans-serif; text-align: center;">Student Records</h1>')
