from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class 自定义注册表单(UserCreationForm):
    昵称 = forms.CharField(required=False, max_length=50)     # required=False表示昵称可以不写
    生日 = forms.DateField(required=False)

    class Meta:
        model = User
        # fields = '__all__'
        fields = ('username', 'password1', 'password2', 'email', '昵称', '生日')  # 用户可以更改的内容





