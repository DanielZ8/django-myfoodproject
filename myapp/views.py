from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def add_food(request):
    return render(request, 'add_food.html')

def search_food(request):
    return render(request, 'search_food.html')

def all_food(request):

    Recipes = Food.objects.all()
    return render(request, 'all_food.html', {'Recipes' : Recipes})