from django.contrib.auth import get_user_model, authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import RegisterSerializer

User = get_user_model()


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(**serializer.validated_data)

        data = RegisterSerializer(user).data

        return Response(data, status=status.HTTP_201_CREATED)

# class LoginView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#         username = serializer.validated_data.get('username')
#         password = serializer.validated_data.get('password')
#
#         user = authenticate(username=username, password=password)
#
#         if user:
#             token, _ = Token.objects.get_or_create(user=user)
#             return Response({"access": token.key}, status=status.HTTP_200_OK)
#
#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

