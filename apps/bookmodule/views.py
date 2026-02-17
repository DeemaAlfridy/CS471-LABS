from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Home Page 🏠")

def books(request):
    return HttpResponse("Books Page 📚")