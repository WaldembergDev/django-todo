from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', views.logout, name='logout'),
    path('my_account/', views.my_account, name='my_account')
]