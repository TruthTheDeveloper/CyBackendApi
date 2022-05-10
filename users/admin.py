from django.contrib import admin

# Register your models here.
from .models import CustomUser
# User = get_user_model()
admin.site.register(CustomUser)