import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, verbose_name='Email')
    username = models.CharField(max_length=100, unique=True, verbose_name='Username')
    first_name = models.CharField(max_length=100, blank=True, null=True, unique=False, verbose_name='First Name')
    last_name = models.CharField(max_length=100, blank=True, null=True, unique=False, verbose_name='Last Name')
    avatar = models.ImageField(blank=True, null=True, upload_to='uploads/avatars', verbose_name='Profile Image')
    is_staff = models.BooleanField(default=False, verbose_name='Staff')
    is_active = models.BooleanField(default=True, verbose_name='Active')
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='Registration Date')
    last_login = models.DateTimeField(blank=True, null=True, verbose_name='Last Login')
    role = models.CharField(
        max_length=50,
        choices=[('student', 'Student'), ('teacher', 'Teacher')],
        default='student'
    )
    interests = models.JSONField(default=list)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    class Meta:
        db_table = 'Users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email


