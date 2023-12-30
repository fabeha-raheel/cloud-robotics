from django.shortcuts import render
from .models import Robot

# Create your views here.

def home(request):
    robots = Robot.objects.all()
    return render(request, 'RosWebApp/frontpg.html', {'robots': robots})

def Turtlebot3(request):
    return render(request, 'RosWebApp/index.html')