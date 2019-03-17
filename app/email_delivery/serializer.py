from rest_framework import serializers
from .models import EmailDelivery


class EmailDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailDelivery
        fields = '__all__'
