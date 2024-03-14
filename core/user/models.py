import uuid
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from core.user.manager.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
  public_id = models.UUIDField(
    db_index=True,
    unique=True,
    default=uuid.uuid4,
    editable=False
  )
  username = models.CharField(
    db_index=True,
    max_length=255,
    unique=True
  )
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.EmailField(
    db_index=True,
    unique=True
  )
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=True)
  is_superuser = models.BooleanField(default=False)
  bio = models.TextField(
    blank=True,
    null=True
  )
  avatar = models.ImageField(
    upload_to='avatars/',
    blank=True,
    null=True
  )
  created = models.DateTimeField(auto_now=True)
  updated = models.DateTimeField(auto_now_add=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']

  objects = UserManager()

  def __str__(self):
    return f"{self.email}"

  @property
  def name(self):
    return f"{self.first_name} {self.last_name}"
