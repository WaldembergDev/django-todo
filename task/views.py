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

@login_required(login_url='account/login')
def edit_task(request, id):
    user = request.user
    task = Task.objects.filter(id = id).filter(user = user).first()
    if request.method == 'GET':
        status = [status.value for status in StatusEnum]
        return render(request, 'edit_task.html', {'task': task, 'status': status})
    else:
        name = request.POST.get('name')
        expiration_date = request.POST.get('expiration_date')
        status = request.POST.get('status')
        task.name = name
        task.expiration_date = expiration_date
        task.status = status
        if not name:
            messages.add_message(request, constants.WARNING, 'O nome não pode ficar vazio!')
            return redirect(f'/task/edit_task/{task.id}')
        if not expiration_date:
            messages.add_message(request, constants.WARNING, 'O prazo da tarefa não pode ficar em branco!')
            return redirect(f'/task/edit_task/{task.id}')
        task.save()
        messages.add_message(request, constants.SUCCESS, 'A tarefa foi editada com sucesso!')
        return redirect(f'/task/edit_task/{task.id}')

@login_required(login_url='account/login')
def exclude_task(request, id):
    user = request.user
    task = Task.objects.filter(id = id).filter(user = user).first()
    task.delete()
    messages.add_message(request, constants.SUCCESS, 'Tarefa excluída com sucesso!')
    return redirect('/task/home')

@login_required(login_url='account/login')
def finish_task(request, id):
    user = request.user
    task = Task.objects.filter(id = id).filter(user = user).first()
    task.status = StatusEnum.FINISHED
    task.save()
    messages.add_message(request, constants.SUCCESS, 'Mensagem atualizada com sucesso!')
    return redirect('/task/home')