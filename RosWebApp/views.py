from django.shortcuts import render
from .models import Robot

# Create your views here.
def home(request):
    robots = Robot.objects.all()
    context = {'robots': robots}
    return render(request, 'RosWebApp/frontpage.html', context)

def robot_page(request, slug):
    robot = Robot.objects.get(robot_slug=slug)
    context = {'robot': robot}
    return render(request, 'RosWebApp/robot_page.html', context)