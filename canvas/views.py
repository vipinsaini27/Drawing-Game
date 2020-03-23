from django.shortcuts import render
from model.views import resetImg

def home(request):
    resetImg()
    return render(request, "canvas/home.html", {})
