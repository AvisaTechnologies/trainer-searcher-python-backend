from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class User(AbstractUser):
    email = models.EmailField(max_length=228, unique=True)

    objects = UserManager()

    def __str__(self):
        return self.email
