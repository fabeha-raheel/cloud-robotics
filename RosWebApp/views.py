from django.shortcuts import render
from .models import Robot

# Create your views here.

# def home(request):
#     robots = Robot.objects.all()
#     return render(request, 'RosWebApp/robopg.html')

def home(request):
    robots = Robot.objects.all()
    return render(request, 'RosWebApp/frontpg.html', {'robots': robots})

def robot_page(request, id, *args, **kwargs):
    robot = Robot.objects.get(id=id)
    print(id, args, kwargs)
    context = {'robot': robot}
    return render(request, 'RosWebApp/index.html', context)