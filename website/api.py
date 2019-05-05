from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from website.models import Get_data, Room  # 得到数据库
# 用户登录管理
from django.contrib.auth.models import User
from django.contrib.auth import login


# class TopmenuXuliehua(serializers.ModelSerializer):
#     class Meta:
#         depth = 1
#         model = Topmenu
#         fields = '__all__'


# class BannerData(serializers.ModelSerializer):
#     class Meta:
#         depth = 1
#         model = Banner
#         # fields = '__all__'
#         fields = ('img',)   # 元组只有一个元素一定要加逗号，或者可以用列表


class Get_Date(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Get_data
        fields = '__all__'


# class Send_Date(serializers.ModelSerializer):
#     class Meta:
#         depth = 1
#         model = Send_data
#         fields = '__all__'


class Room_Admin(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Room
        fields = '__all__'


@api_view(['GET', 'POST'])
def indexData(request):
    # 首页的导航栏
    # topmenu = Topmenu.objects.all()
    # topmenuData = TopmenuXuliehua(topmenu, many=True)
    #
    # # 首页的Banner
    # banner = Banner.objects.all()
    # bannerData = BannerData(banner, many=True)

    # MCU的数据
    get_data = Get_data.objects.all()
    getData = Get_Date(get_data, many=True)

    # # 发送给MCU的指令
    # send_data = Send_data.objects.all()
    # sendData = Send_Date(send_data, many=True)

    # 房间管理
    room_data = Room.objects.all()
    roomData= Room_Admin(room_data, many=True)

    return Response({'get_data': getData.data, 'room_admin': roomData.data})


# def roomdata():
#     room_data = Room.objects.all()
#     roomData = Room_Admin(room_data, many=True)
#     data = str({'room_admin': roomData.data})
#     return data


