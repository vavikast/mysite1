from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'felix/index.html')


def login(request):
    return render(request, 'felix/login.html')


def register(request):
    return render(request, 'felix/register.html')


def logout(request):
    return redirect("/")