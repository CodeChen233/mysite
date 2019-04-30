from django.contrib import admin
from website.models import Topmenu, Banner, Get_data  # 引入自己创建的APP实例模板

# Register your models here.

admin.site.register(Topmenu)
admin.site.register(Banner)
admin.site.register(Get_data)
# 如上操作后记得合并数据库  python manage.py makemigrations，python manage.py migrate


















