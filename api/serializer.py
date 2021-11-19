from rest_framework import serializers
from . models import Contact

#Creating model serializers.
class ContactSerializer(serializers.ModelSerializer):
    """Serializer class for our contact model based on model-serializer"""
    class Meta:
        model = Contact
        fields = ["id", "name", "phone_number", "email"]