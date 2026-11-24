from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import CASCADE

from reviews.additional import scam_messages


# Create your models here.


class Review(models.Model):
    class RatingChoices(models.IntegerChoices):
        TERRIBLE = 1, 'Terrible'
        BAD = 2, 'Bad'
        OK = 3, 'Ok'
        GOOD = 4, 'Good'
        EXCELLENT = 5, 'Excellent'
    employee = models.ForeignKey(
        to='employees.Employee',
        related_name='reviews',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews',
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(
        validators=[MinLengthValidator(10)]
    )
    rating = models.SmallIntegerField(choices=RatingChoices.choices)

    class Meta:
        ordering = ['-created_at']
        permissions = [
            ('can_edit_reviews', 'can edit reviews')
        ]

    def save(self, *args, **kwargs):
        if not self.id:
            self.text = scam_messages(self.rating, self.text)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.text
