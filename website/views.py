from django.shortcuts import render, HttpResponse, redirect
import socket
# Create your views here.


def home(request):
    return render(request, 'home.html')


def now_time_data(request):
    return render(request, 'now_time_data.html')


def history_data(request):
    return render(request, 'history_data.html')


def air_cdtion_ctr(request):
    sk = socket.socket()
    address = ('10.14.30.127', 60000)  # 公网
    sk.connect(address)
    if request.method == "POST":
        floor = request.POST.get("floor", None)
        room = request.POST.get("room", None)
        status = request.POST.get("air_cdtin_ctr", None)

        data = str([{'floor': floor}, {'room': room}, {'status': status}])

        sk.send(bytes(data, 'utf8'))

    sk.close()

    return render(request, 'air_cdtion_ctr.html')


def room_check(request):
    if request.method == "POST":
        floor = request.POST.get("floor", None)
        room = request.POST.get("room", None)
        data = int(floor) * 10 + int(room)
        if data is None:
            return render(request, 'room_check.html', {'error': '输入为空！'})
        else:
            url = '/admin/website/room/' + str(data)
            return redirect(url)
    else:
        return render(request, 'room_check.html')


