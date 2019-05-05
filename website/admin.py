from django.contrib import admin
from website.models import Get_data, Room  # 引入自己创建的APP实例模板

# Register your models here.

admin.site.register(Get_data)
admin.site.register(Room)
# 如上操作后记得合并数据库  python manage.py makemigrations，python manage.py migrate


















