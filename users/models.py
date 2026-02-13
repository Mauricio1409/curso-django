from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    class UserRole(models.TextChoices):
        AUTOR = 'autor', 'autor'
        USER = 'user', 'User'

    role = models.CharField(max_length=20, choices=UserRole.choices, default=UserRole.USER)

