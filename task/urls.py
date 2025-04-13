from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('create_task/', views.create_task, name='create_task'),
    path('edit_task/<int:id>', views.edit_task, name='edit_task'),
    path('exclude_task/<int:id>', views.exclude_task, name='exclude_task'),
    path('finish_task/<int:id>', views.finish_task, name='finish_task')
]