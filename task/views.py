from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import StatusEnum, Task
from django.contrib import messages
from django.contrib.messages import constants
from account.models import User

# Create your views here.
@login_required(login_url='/account/login')
def home(request):
    status = [status.value for status in StatusEnum]
    user = request.user
    tasks = Task.objects.filter(user = user).all()
    return render(request, 'home.html', {'status': status, 'tasks': tasks})

@login_required(login_url='/account/login')
def create_task(request):
    if request.method == 'GET':
        status = [status.value for status in StatusEnum]
        return render(request, 'create_task.html', {'status': status})
    else:
        name = request.POST.get('name')
        expiration_date = request.POST.get('expiration_date')
        status = request.POST.get('status')
        if not name:
            messages.add_message(request, constants.WARNING, 'O nome não pode ficar em branco')
            return redirect('/task/create_task/')
        if not expiration_date:
            messages.add_message(request, constants.WARNING, 'A data não pode ficar em branco')
            return redirect('task/create_task/')
        user = request.user
        task = Task(
            name = name,
            expiration_date = expiration_date,
            status = status,
            user = user
        )
        task.save()
        return redirect('/task/create_task/')