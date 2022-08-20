from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from .forms import ClientCreationForm, ClientAuthenticationForm


def register_user(request):
    context = {}
    if request.POST:
        form = ClientCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username', '')
            password = request.POST.get('password1', '')
            account = authenticate(username=username, password=password)
            login(request, account)
            messages.success(request, 'You successfully signed up!')
            return redirect('home_page')
    else:
        form = ClientCreationForm()
        context['form'] = form
    return render(request, 'client/register.html', context)


def login_user(request):
    context = {}
    if request.POST:
        form = ClientAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            client = authenticate(username=username, password=password)
            if client:
                login(request, client)
                messages.success(request, 'You successfully signed in!')
                return redirect('home_page')
        else:
            context['form'] = form
    else:
        form = ClientAuthenticationForm()
        context['form'] = form
    return render(request, 'client/login.html', context)


def logout_user(request):
    logout(request)
    messages.success(request, 'You successfully logged out!')
    return redirect('home_page')
