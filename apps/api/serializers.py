from rest_framework import serializers
from .models import User, Todo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number','created_at', 'password',]
        # REgister
class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=255, write_only=True, label='Подтверждения пароля')
    class Meta:
        model = User 
        fields = ['id', 'username','email','password', 'confirm_password']
        
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password':'Пароли отличаются'})
        return attrs 
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'] 
            
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'is_completed', 'created_at', 'image']
