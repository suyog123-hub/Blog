# serializers.py

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name  = serializers.CharField(max_length=30)
    username   = serializers.CharField(max_length=150)
    password   = serializers.CharField(write_only=True, min_length=8)

    def validate_username(self, value):
        
        if User.objects.filter(username=value.lower()).exists():
            raise serializers.ValidationError("Username already taken.")
        return value.lower()                 

    def create(self, validated_data):
        user = User.objects.create_user(
            username   = validated_data["username"],  
            password   = validated_data["password"],
            first_name = validated_data["first_name"],
            last_name  = validated_data["last_name"],
        )
        return user


class LoginSerializer(serializers.Serializer): 
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True, min_length=8)

    def validate(self, data):
        username = data.get("username", "").lower()
        password = data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError(
                "Invalid credentials."           
            )

        refresh = RefreshToken.for_user(user)  
        return {
            "tokens": {
                "refresh": str(refresh),
                "access":  str(refresh.access_token),  
            },
        }