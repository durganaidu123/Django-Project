from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.http import JsonResponse
from .rectangle import Rectangle

def rectangle_view(request):
    # Create a Rectangle instance with example values
    rect = Rectangle(length=10, width=5)

    # Prepare data to be returned as JSON
    data = list(rect)
    return JsonResponse(data, safe=False)

