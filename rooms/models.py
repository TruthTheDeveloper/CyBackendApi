from django.db import models

# Create your models here.



class Rooms(models.Model):
    room_type = models.CharField(max_length=500)
    room_description = models.CharField(max_length=1000)
    room_price = models.CharField(max_length=50)
    roomImage = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room_type

    class Meta:
        ordering = ("created_at",)
    