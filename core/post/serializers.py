from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from core.abstract.serializers import AbstractSerializer
from core.post.models import Post
from core.user.models import User
from core.user.serializers import UserSerializer

class PostSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='public_id'
    )

    def validate_author(self, value):
        if self.context["request"].user != value:
            raise ValidationError("You can't create a post for another user.")
        return value

    class Meta:
        model = Post
        # List of all the fields that can be included in a
        # request or a response
        fields = [
            'id',
            'author',
            'body',
            'edited',
            'created',
            'updated'
        ]
        read_only_fields = ["edited"]

    def to_representation(self, instance):
        # Llama al método to_representation de la clase base
        rep = super().to_representation(instance)

        # Modifica el campo 'author' en la representación
        author = User.objects.get_object_by_public_id(rep["author"])
        rep["author"] = UserSerializer(author).data

        return rep