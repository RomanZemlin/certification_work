from rest_framework import serializers
from .models import User
import bcrypt


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Пользователь с такой электронной почтой уже существует.")

        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user = User.objects.create(password=hashed_password, **validated_data)
        return user

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'image']
