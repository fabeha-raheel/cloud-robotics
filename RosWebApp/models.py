from django.db import models

# Create your models here.
class Robot(models.Model):
    robot_name = models.CharField(max_length=30)
    robot_type = models.CharField(max_length=30)
    robot_slug = models.SlugField(unique=True) 
    robot_icon = models.ImageField(upload_to='RosWebApp/images', default='')

    def __str__(self):
        return self.robot_name