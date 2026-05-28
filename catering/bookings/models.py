from django.db import models

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending',   'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    name       = models.CharField(max_length=100)
    email      = models.EmailField()
    phone      = models.CharField(max_length=20)
    event_type = models.CharField(max_length=100)
    event_date = models.DateField()
    package    = models.CharField(max_length=100)
    status     = models.CharField(
                     max_length=20,
                     choices=STATUS_CHOICES,
                     default='pending'
                 )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.event_type}"


class Message(models.Model):
    name       = models.CharField(max_length=100)
    email      = models.EmailField()
    message    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"


