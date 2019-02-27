from django.shortcuts import render, get_object_or_404
from .models import WineInfo

def index(request):
    return render(request,'index.html')

def recommend(request):
    return render(request,'recommend.html')

def quality(request):
    return render(request,'quality.html')
