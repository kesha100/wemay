from django.contrib.auth import authenticate, logout, login

from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.response import Response
from rest_framework import status

from django.db import utils as django_utils
from user.api import serializers as ser
from user.models import MyUser


# Create your views here.


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = ser.RegisterSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Вы успешно зарегестрировались!"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(f'ошибочка: {e}')
            return Response({'message': 'Оишбочка в реге'})
        except django_utils.IntegrityError:
            return Response({'error': 'Харош, придумай другой email'}, status=status.HTTP_400_BAD_REQUEST)


class LogInView(APIView):
    def post(self, request):
        serializer = ser.LogInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(f"Serializer data: {serializer.validated_data}")
        user = authenticate(**serializer.validated_data)
        print(user)
        if user:
            login(request, user)
            access_token = AccessToken.for_user(user)
            refresh_token = RefreshToken.for_user(user)

            print(f"Access Token: {access_token}")
            print(f"Refresh Token: {refresh_token}")

            return Response(data={"message": "Вход в систему выполнен успешно",
                                  "access": str(access_token),
                                  "refresh": str(refresh_token),
                                  }
                            )
        else:
            return Response({'detail': 'Неверные данные, попробуйте ещё раз!'}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # Perform logout
        logout(request)

        return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
