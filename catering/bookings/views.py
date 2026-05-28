from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Booking, Message
from .serializers import BookingSerializer, MessageSerializer


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_queryset(self):
        return Booking.objects.all().order_by('-created_at')


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_queryset(self):
        return Message.objects.all().order_by('-created_at')

# Create your views here.
