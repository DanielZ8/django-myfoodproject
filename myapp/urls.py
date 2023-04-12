from django.urls import path
from . import views


urlpatterns = [
        path('', views.index, name = 'index'),
        path('login', views.login, name = 'login'),
        path('register', views.register, name = 'register'),
        path('add_food', views.add_food, name = 'add_food'),
        path('search_food', views.search_food, name = 'search_food'),
        path('all_food', views.all_food, name='all_food'),
]