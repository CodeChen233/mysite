from django.db import models


# Create your models here.


class Topmenu(models.Model):      # 创建Model 数据库层  顶部目录

    title = models.CharField(default='', blank=True, null=True, max_length=20)  # Django model字段类型，可自行百度
    url = models.CharField(default='', blank=True, null=True, max_length=20)

    def __str__(self):
        return self.title


class Banner(models.Model):       # 创建Model 数据库层  轮播图
    img = models.ImageField(blank=True, null=True)   # Django model字段类型，可自行百度

    def __int__(self):
        return self.id


class Get_data(models.Model):    # 用于接收单片机数据
    get_data = models.CharField(default='', blank=True, null=True, max_length=20)

    def __str__(self):
        return self.get_data




