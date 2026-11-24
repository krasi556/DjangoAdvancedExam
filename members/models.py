from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Sum

# Create your models here.

UserModel = get_user_model()


class Endorsement(models.Model):
    sponsor = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='endorsement_given'
    )
    employee = models.ForeignKey(
        to='employees.Employee',
        on_delete=models.CASCADE,
        related_name='endorsements_received'
    )
    amount = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        validators=[MinValueValidator(1)]
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )