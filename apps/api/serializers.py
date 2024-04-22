from rest_framework import serializers
from .models import User, Todo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'age', 'created_at', 'password',]

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'is_completed', 'created_at', 'image']
