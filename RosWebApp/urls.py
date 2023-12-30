from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('tb3/', views.Turtlebot3, name='Turtlebot3'), 
]