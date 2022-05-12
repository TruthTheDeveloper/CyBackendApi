from django.db import models
from django.utils import timezone

# Create your models here.


class UserInfo(models.Model):


    TITLES = (
        ("MR", "MR"),
        ("Mrs", "Mrs"),
        ("Chief", "Chief"),
        ("Dr", "Dr"),
        ("Engr", "Engr"),
        ("senator", "Senator"),
        ("Arch", "Arch"),
        ("Bar", "Barr")
    )


    title = models.CharField(max_length=50,choices=TITLES)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    x_reservation = models.BooleanField(null=True)
    discount_code = models.CharField(max_length=200, blank=True)
    check_in = models.CharField(max_length=200)
    check_out = models.CharField(max_length=200)
    payment_status = models.BooleanField()
    confirm_user_lodge = models.BooleanField()
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title + " " + self.first_name + " " + self.last_name

    class Meta:
        ordering = ("created_at",)