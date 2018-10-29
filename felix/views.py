from django.shortcuts import render
from django.shortcuts import redirect
from . import models

# Create your views here.
def index(request):
    return render(request, 'felix/index.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        message = "所有字段必须填写"
        if username and password:  # 确保用户名和密码都不为空
            username = username.strip()
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    return redirect('')
                else:
                    message = "密码不正确"

            except:
                message = "用户名不存在！"
        return render(request, 'felix/login.html', {"message": message})
    return render(request, 'felix/login.html')



def register(request):
    return render(request, 'felix/register.html')


def logout(request):
    return redirect("/")