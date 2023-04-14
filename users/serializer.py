from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)#not return password

    class Meta:
        fields = '__all__'
    
    def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
            )
        
        user.set_password(validated_data['password'])
        user.save()
        return user