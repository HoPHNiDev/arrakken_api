from rest_framework import serializers
from .models import api_model
class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = api_model
        fields = ["telegram_user_id", 'for_user']