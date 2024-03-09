from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Student_Fee(request):
    return HttpResponse('<h1 style="color: #FF5999; font-size: 36px; font-family: Arial, sans-serif; text-align: center;">Student Fee</h1>')

def Student_Fee_Detail(request):
    return HttpResponse('<h1 style="color: #FF5999; font-size: 36px; font-family: Arial, sans-serif; text-align: center;">Student Fee Detail</h1>')
