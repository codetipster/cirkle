from rest_framework import serializers
from . models import Contact, UserProfile
from rest_framework.authtoken.models import Token

#Creating model serializers.


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer class for our userprofile model based on model-serializer"""
    class Meta:
        model = UserProfile
        fields = ["id", "email", "password"]
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        """creating new users and their access tokens"""
        user = UserProfile.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user    


class ContactSerializer(serializers.ModelSerializer):
    """Serializer class for our contact model based on model-serializer"""
    class Meta:
        model = Contact
        fields = ["id", "name", "phone_number", "email"]