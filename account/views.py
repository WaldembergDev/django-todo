from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        pass
        

def cadastro(request):
    if request.method == 'GET':
        status = request.GET.get('status')
        return render(request, 'cadastro.html', {'status': status})
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(name = name, password = password)
        if user.exists():
            return redirect('/account/cadastro/?status=error_1')
        else:
            User.objects.create_user(name = name, email = email, password = password)
            return redirect('/account/cadastro/?status=success')
            