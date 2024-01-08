from django.urls import path
from . import views

urlpatterns = [
    path('', views.df_tank, name='df_tank'),
    # path('robot/<slug:slug>/', views.robot_page, name='robot_page'),
]