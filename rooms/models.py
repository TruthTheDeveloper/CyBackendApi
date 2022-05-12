from django.utils import timezone
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.



class Room(models.Model):
    room_type = models.CharField(max_length=500)
    room_description = models.CharField(max_length=1000)
    room_price = models.CharField(max_length=50)
    room_Image = CloudinaryField('image', null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.room_type

    class Meta:
        ordering = ("created_at",)
    