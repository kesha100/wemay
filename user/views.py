from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import MyUser
from .serializers import RegisterSerializer, LogInSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        try:
            if serializer.is_valid():
                email = serializer.validated_data['email']
                if MyUser.objects.filter(email=email).exists():
                    raise ValueError("Этот email уже используется!")
                serializer.save()
                return Response({"message": "Вы успешно зарегестрировались!"}, status=status.HTTP_201_CREATED)
            return Response({"message": "Ошибка при регистрации!"}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError as e:
            print(f'Error: {e}')
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class LogInView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        # Basic validation
        if not email or not password:
            return Response({'error': 'Both username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, email=email, password=password)

        if user is not None and user.is_active:
            login(request, user)

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({'access_token': access_token}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials or inactive account'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Perform logout
        logout(request)

        return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)