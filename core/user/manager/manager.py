from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

class UserManager(BaseUserManager):

  def get_object_by_public_id(self, public_id):
    try:
      instance = self.get(public_id=public_id)
      return instance
    except (ObjectDoesNotExist, ValueError, TypeError):
      return Http404

  def create_user(self, username, email, password=None, **kwargs):
    """Create and return a `User` with an email, phone
    number, username and password."""
    if username is None:
      raise TypeError('Users must have a username.')
    if email is None:
      raise TypeError('Users must have an email.')
    if password is None:
      raise TypeError('User must have an email.')
    user = self.model(username=username,
    email=self.normalize_email(email), **kwargs)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, username, email, password, **kwargs):
    """
    Create and return a `User` with superuser (admin)
    permissions.
    """
    if password is None:
      raise TypeError('Superusers must have a password.')
    if email is None:
      raise TypeError('Superusers must have an email.')
    if username is None:
      raise TypeError('Superusers must have an username.')
    user = self.create_user(username, email, password, **kwargs)
    user.is_superuser = True
    user.is_staff = True
    user.save(using=self._db)
