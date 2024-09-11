from .models import User
from rest_framework import serializers
#create,validate password and validate email
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password1 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password1']

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
        )
        user.is_active=False
        user.save()
        return user
    
    def validate(self, data):
        if data['password'] != data['password1']:
            raise serializers.ValidationError("Passwords didn't match")
        return data
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email already exists")
        return value
    
class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=255,read_only=True)
    password = serializers.CharField(max_length=255, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'password']