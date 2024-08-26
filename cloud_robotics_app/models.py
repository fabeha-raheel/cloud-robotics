from django.db import models

# Create your models here.

class Robot(models.Model):
    TURTLEBOT = 'Turtlebot'
    UAV_COPTER = 'UAV-Copter'
    UGV_ROVER = 'UGV-Rover'
    MOBILE_ROBOT = 'Mobile-Robot'

    ROBOT_TYPE_CHOICES = [
        (TURTLEBOT, 'Turtlebot'),
        (UAV_COPTER, 'UAV-Copter'),
        (UGV_ROVER, 'UGV-Rover'),
        (MOBILE_ROBOT, 'Mobile-Robot'),
    ]

    robot_name = models.CharField(max_length=30)
    robot_type = models.CharField(max_length=30, choices=ROBOT_TYPE_CHOICES)
    robot_slug = models.SlugField(unique=True)
    robot_icon = models.ImageField(upload_to='RosWebApp/images', default='')

    def __str__(self):
        return self.robot_name