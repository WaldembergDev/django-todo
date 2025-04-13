from django.shortcuts import render, redirect
from .models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not email:
            messages.add_message(request, constants.WARNING, 'Informe um e-mail!')
            return redirect('/account/login')
        if not password:
            messages.add_message(request, constants.WARNING, 'Informe uma senha!')
            return redirect('/account/login')
        user = auth.authenticate(request, email = email, password = password)
        if user:
            auth.login(request, user)
            return redirect('/task/home')
        else:
            messages.add_message(request, constants.WARNING, 'E-mail ou senha inválidos!')
            return redirect('/account/login')
        

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email = email)
        if not name:
            messages.add_message(request, constants.WARNING, 'O campo nome não pode ficar em branco!')
            return redirect('/account/cadastro')
        if not email:
            messages.add_message(request, constants.WARNING, 'O campo email não pode ficar em branco!')
            return redirect('/aacount/cadastro')
        if user.exists():
            messages.add_message(request, constants.WARNING, 'Já existe um usuário com esse e-mail!')
            return redirect('/account/cadastro/')
        else:
            User.objects.create_user(name = name, email = email, password = password)
            messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso!')
            return redirect('/account/cadastro/')

def logout(request):
    auth.logout(request)
    return redirect('/account/login')


@login_required(login_url='/account/login')
def my_account(request):
    if request.method == 'GET':
        return render(request, 'my_account.html')
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        if not name:
            messages.add_message(request, constants.WARNING, 'O nome não pode ficar em branco!')
            return redirect('/account/my_account')
        if not email:
            messages.add_message(request, constants.WARNING, 'O email não pode ficar em branco!')
            return redirect('/account/my_account')
        user = request.user
        user.name = name
        user.email = email
        user.save()
        messages.add_message(request, constants.SUCCESS, 'Seu cadastro foi atualizado com sucesso!')
        return redirect('/account/my_account')