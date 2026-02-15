from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer, UserSerializer


User = get_user_model()

class RegisterSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password', 'role')
        read_only_fields = ('id',)


class CustomUserSerializer(UserSerializer):

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'role')
        read_only_fields = ('id',)