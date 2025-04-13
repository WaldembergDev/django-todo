from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('create_task/', views.create_task, name='create_task')
]