from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from .forms import UserLoginForm,UserRegisterForm
def login_site(request):
    next = request.GET.get('next')
    print(request.GET)
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        login(request, user)
        if next:
            redirect(next)
        return redirect('catalog:index')
    context = {'form':form}
    return render(request, 'authentication/login.html', context)

def logout_site(request):
    logout(request)
    redirect('/')
    form = UserLoginForm(request.POST or None)
    context = {'form':form}
    return render(request, 'authentication/login.html', context)
