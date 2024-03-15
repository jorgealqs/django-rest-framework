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
  posts_liked = models.ManyToManyField(
    "core_post.Post",
    related_name="liked_by"
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

  def like(self, post):
    """Like `post` if it hasn't been done yet"""
    return self.posts_liked.add(post)

  def remove_like(self, post):
    """Remove a like from a `post`"""
    return self.posts_liked.remove(post)

  def has_liked(self, post):
    """Return True if the user has liked a `post`; else
    False"""
    return self.posts_liked.filter(pk=post.pk).exists()
