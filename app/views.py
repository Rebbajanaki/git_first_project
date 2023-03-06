from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def sample(request):
    return HttpResponse('<marquee><h1>good morning</h1><marquee>')