from django.db import models


# Create your models here.


class Get_data(models.Model):    # 用于接收单片机数据
    get_data = models.CharField(default='', blank=True, null=True, max_length=20)

    def __str__(self):
        return self.get_data


class Room(models.Model):  # 房间管理
    floor = models.CharField(default='', blank=True, null=True, max_length=20)
    room = models.CharField(default='', blank=True, null=True, max_length=20)
    status = models.BooleanField(blank=True)

    def __str__(self):
        return self.room


