from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def recommend(request):
    return render(request,'recommend.html')

def quality(request):
    return render(request,'quality.html')
