from django.shortcuts import render
from model.views import resetImg

def draw(request):
    resetImg()
    return render(request, "canvas/draw.html", {})
