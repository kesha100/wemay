from rest_framework import serializers
from user.models import MyUser


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=3, max_length=20, write_only=True)

    def create(self, validated_data):
        user = MyUser.objects.create(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class LogInSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=3, max_length=20, write_only=True)



