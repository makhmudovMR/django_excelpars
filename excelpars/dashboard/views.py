from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from .models import ObjectInfo



def home(request):
    return render(request, 'dashboard/home.html', {'text': 'home'})


def login_view(request):
    form = LoginForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('http://127.0.0.1:8000/dashboard/panel')

    return render(request, 'dashboard/login.html', {'form': form})


@login_required
def panel(request):
    data = ObjectInfo.objects.all()
    return render(request, 'dashboard/panel.html', {'data': data})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('http://127.0.0.1:8000/dashboard/login')