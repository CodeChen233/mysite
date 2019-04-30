# __author: gy-chen
# data: 2019/4/23
# -*- coding: UTF-8 -*-
# https://www.cnblogs.com/alex3714/articles/5885096.html

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from website.models import Topmenu, Banner, Get_data  # 得到数据库
# 用户登录管理
from django.contrib.auth.models import User
from django.contrib.auth import login


class TopmenuXuliehua(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Topmenu
        fields = '__all__'


class BannerData(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Banner
        # fields = '__all__'
        fields = ('img',)   # 元组只有一个元素一定要加逗号，或者可以用列表


class Get_Date(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Get_data
        fields = '__all__'


@api_view(['GET', 'POST'])
def indexData(request):
    # 首页的导航栏
    topmenu = Topmenu.objects.all()
    topmenuData = TopmenuXuliehua(topmenu, many=True)

    # 首页的Banner
    banner = Banner.objects.all()
    bannerData = BannerData(banner, many=True)

    # MCU的数据
    get_data = Get_data.objects.all()
    getData = Get_Date(get_data, many=True)

    return Response({'topmenu': topmenuData.data, 'banner': bannerData.data, 'get_data': getData.data})






