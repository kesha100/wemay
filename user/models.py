from django.contrib.auth.models import AbstractUser
from django.db import models

from user.api.managers import MyUserManager
from user.utils.utils import user_image_path


class MyUser(AbstractUser):
    username = models.CharField(unique=True, max_length=50, null=True)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to=user_image_path, default=None, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyUserManager()

    def __str__(self):
        return self.email
