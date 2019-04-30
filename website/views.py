from django.shortcuts import render, HttpResponse
from website.models import Topmenu, Get_data
from MCU.socket import start_socket
from django.contrib.auth.models import User  # 用于登录
# Create your views here.


def home(request):
    # topmenu =Topmenu.objects.all()   这里不需要再用这个方法了，这个交给vue.js做了,通过AJAX,在api.py里实现
    get_data = Get_data.objects.all()  # 这层也可以不需要
    # mydata = '110'

    context = {
        # 'topmenu': topmenu,
        'get_data': get_data,        # 这里的数据是通过Django渲染到模板上去的
        # 'mydata': mydata

    }   # 创建的MODEL层数据库
    return render(request, 'home.html', context)


def MCU_data(request):
    start_socket()
    # return render(request, 'index1.html')
    return HttpResponse(12)


def now_time_data(request):
    return render(request, 'now_time_data.html')


def history_data(request):
    return render(request, 'history_data.html')



