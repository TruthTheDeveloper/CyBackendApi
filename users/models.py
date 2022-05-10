from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils.text import slugify
from .utils import utils
import uuid




class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """

        # if not extra_fields.get('phone_number') == 0:
        #     raise ValueError('please input phone number')

        # print(phone_number, 'phone')
        if not email:
            raise ValueError('Users must have an email address')

        

        user = self.model(
            email=self.normalize_email(email),
            # phone_numbaer= extra_fields.get('phone_number'),
        )

        # user.phone_number = 333333

        print(user, 'user')

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email,  password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=100, default="")
    phone_number = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    slug = models.SlugField(max_length=255, unique=True)


    objects = UserManager()

    
    def save(self, *args, **kwargs):
        # self.phone_number = 134
        print(self.phone_number, 'before') #this return None
        if not self.slug:
            self.slug = slugify(utils.rand_slug() + "-" + self.username)
        super(CustomUser, self).save(*args, **kwargs)
        print(self.phone_number, 'after') #this return None

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number'] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def owner(self):
        return self.user

    


    