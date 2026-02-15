import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser, PermissionsMixin):
    class UserRole(models.TextChoices):
        AUTOR = 'autor', 'autor'
        USER = 'user', 'User'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=20, choices=UserRole.choices, default=UserRole.USER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.email

