from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BookingViewSet, MessageViewSet

router = DefaultRouter()
router.register(r'bookings', BookingViewSet, basename='booking')
router.register(r'messages', MessageViewSet, basename='message')

urlpatterns = [
    path('', include(router.urls)),
]