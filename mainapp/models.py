from django.contrib.auth.models import User, AbstractUser
from django.conf import settings
from django.db import models


class MyUser(AbstractUser):

    def __str__(self):
        return self.username

    # super().REQUIRED_FIELDS = ["email", "first_name", "last_name"]
