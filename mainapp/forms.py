from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ("first_name", "last_name", "username", "email", "password1", "password1")


class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = MyUser
        fields = ("first_name", "last_name", "username", "email", "password")
