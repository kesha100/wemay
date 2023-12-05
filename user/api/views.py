from django.contrib.auth import authenticate, logout, login

from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.response import Response
from rest_framework import status

from django.db import utils as django_utils
from user.api import serializers as ser

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
        user = authenticate(request, **serializer.validated_data)

        if user:
            login(request, user)
            return Response(data={"message": "Вход в систему выполнен успешно",
                                  "access": str(AccessToken.for_user(user)),
                                  "refresh": str(RefreshToken.for_user(user)),
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
