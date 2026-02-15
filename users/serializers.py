from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers


User = get_user_model()

class RegisterSerializer(UserCreateSerializer):
    role = serializers.ChoiceField(choices=User.UserRole, default=User.UserRole.USER)
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password', 'role')
        read_only_fields = ('id',)

class CustomUserSerializer(UserSerializer):

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'role')
        read_only_fields = ('id',)