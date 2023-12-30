from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('robot/<int:id>/', views.robot_page, name='robot_page'),
]