from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        SUPERUSER = 'superuser', 'Superuser'
        ADMIN = 'admin', 'Admin'
        STAFF = 'staff', 'Staff'
        USER = 'user', 'User'

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.USER,
        verbose_name='Rol',
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"