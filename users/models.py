from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRoles(models.TextChoices):
    MEMBER = 'member'
    MODERATOR = 'moderator'


class User(AbstractUser):
    role = models.CharField(max_length=15, verbose_name='роль', choices=UserRoles.choices, default=UserRoles.MEMBER)
