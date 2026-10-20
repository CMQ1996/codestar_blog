from django.shortcuts import render
from django.http import HttpResponse   # ← add this line

# Create your views here.

def index(request):
    return HttpResponse("Hello, world!")