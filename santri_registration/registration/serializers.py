# registration/serializers.py
from rest_framework import serializers
from .models import Santri

class SantriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Santri
        fields = '__all__'
