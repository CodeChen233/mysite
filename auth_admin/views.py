from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout     # 验证，登录，登出
from django.contrib.auth.forms import UserCreationForm    # 创建用户表单
from .forms import 自定义注册表单
from .models import 普通会员表
# Create your views here.


def index(request):
    return render(request, 'index.html')


def My_login(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['用户名'], password=request.POST['密码'])
        if user is None:
            return render(request, 'login.html', {'error': '用户名不存在或密码错误！'})
        else:
            login(request, user)
            return redirect('/home')
    else:
        return render(request, 'login.html')


def My_logout(request):
    logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        register_form = 自定义注册表单(request.POST)
        if register_form.is_valid():     # 如果验证表单失败，则直接跳到context及以下
            register_form.save()
            user = authenticate(username=register_form.cleaned_data['username'],
                                password=register_form.cleaned_data['password1'])
            user.email = register_form.cleaned_data['email']
            普通会员表(用户=user, 昵称=register_form.cleaned_data['昵称'],
                  生日=register_form.cleaned_data['生日']).save()

            return redirect('/register_success')
    else:
        # 创建注册表单
        register_form = 自定义注册表单()
    context = {'register_form': register_form}
    return render(request, 'register.html', context)


def register_success(request):
    return render(request, 'register_success.html')


