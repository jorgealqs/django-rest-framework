from core.user.models import User
from core.abstract.serializers import AbstractSerializer
from django.conf import settings
from rest_framework import serializers

class UserSerializer(AbstractSerializer):
  posts_count = serializers.SerializerMethodField()
  default_avatar_url = serializers.SerializerMethodField()

  class Meta:
    model = User
    fields = [
      'id',
      'username',
      'first_name',
      'last_name',
      'bio',
      'avatar',
      'email',
      'is_active',
      'password',
      'posts_count',
      'created',
      'updated',
      'default_avatar_url',
    ]
    read_only_field = ['is_active']

  def to_representation(self, instance):
    representation = super().to_representation(instance)
    if not representation['avatar']:
      representation['avatar'] = settings.DEFAULT_AVATAR_URL
      representation['default_avatar'] = True
    else:
      request = self.context.get('request')
      if request:
        representation['avatar'] = request.build_absolute_uri(representation['avatar'])
      representation['default_avatar'] = False
    return representation


  def get_posts_count(self, obj):
    return obj.post_set.count()

  def get_default_avatar_url(self, obj):
    return settings.DEFAULT_AVATAR_URL
