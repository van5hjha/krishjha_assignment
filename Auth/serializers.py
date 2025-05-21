from rest_framework import serializers
from django.contrib.auth.models import User
class RegisterUserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(write_only = True)
    email = serializers.EmailField()
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ["name", "email", "password"]
    
    def validate_email(self, value):
        if User.objects.filter(email = value).exists():
            raise serializers.ValidationError("Email already exists!")
        return value
    
    def create(self, validated_data):
        name = validated_data.pop("name")
        user = User.objects.create(username = validated_data["email"], email = validated_data["email"], first_name = name)
        user.set_password(validated_data["password"])
        user.save()
        return user

