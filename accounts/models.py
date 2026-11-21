from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


# from accounts.managers import NewUserManager


# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)


class Profile(models.Model):

    """
    this will be for the basic profile that everyone will have it

    """

    is_vip = models.BooleanField(default=False)

    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,

    )
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)

    @property
    def full_name(self):
        if not self.first_name and not self.last_name:
            return None
        return f'{self.first_name} {self.last_name}'

    bio = models.TextField(null=True)
    date_of_birth = models.DateField(
        null=True,
        blank=True
    )
    profile_pic = models.ImageField(
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField(default=0)

# class NewUser(AbstractBaseUser, PermissionsMixin):
#
#     USERNAME_FIELD = 'email'
#
#     email = models.EmailField(
#         unique=True,
#     )
#
#     objects = NewUserManager()
