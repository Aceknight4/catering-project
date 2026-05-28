from rest_framework import serializers
from .models import Booking, Message


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Booking
        fields = [
            'id',
            'name',
            'email',
            'phone',
            'event_type',
            'event_date',
            'package',
            'status',
            'created_at',
        ]
        read_only_fields = ['created_at']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Message
        fields = [
            'id',
            'name',
            'email',
            'message',
            'created_at',
        ]
        read_only_fields = ['created_at']