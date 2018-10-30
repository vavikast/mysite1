from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms

# Create your views here.
def index(request):
    return render(request, 'felix/index.html')


def login(request):
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    return redirect('')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'felix/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'felix/login.html', locals())



def register(request):
    return render(request, 'felix/register.html')


def logout(request):
    return redirect("/")