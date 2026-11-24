from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models





# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)


class Profile(models.Model):
    """
    this will be for the basic profile that everyone will have it

    """

    class VipStatus(models.TextChoices):
        PLEB = 'pleb', 'Pleb'
        SUPER_SPONSOR = 'super_sponsor', 'Super Sponsor'
        INNER_CIRCLE = 'inner_circle', 'Inner Circle'
        NO_LIFER = 'no_lifer' , 'No Lifer'

    tier = models.CharField(
        max_length=100,
        default=VipStatus.PLEB,
        choices=VipStatus.choices

    )

    total_wasted = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        default=0.00


    )
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,

    )
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True) \


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
