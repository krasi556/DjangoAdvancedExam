from django import forms
from django.core.exceptions import ValidationError

from reviews.models import Review


class ReviewForms(forms.ModelForm):
    text = forms.CharField(
        min_length=10,
        widget=forms.Textarea(attrs={
            'rows': 2
        }),
        error_messages={
            'min_length':'At least do try to form a 10 letter word',
            'required':'You gonna leave it empty like that ?'
        }
    )

    class Meta:
        model = Review
        fields = ['rating', 'text']
        error_messages = {
            'rating':{
                'required':'At least choose a rating '
            }
        }
    def clean_text(self):
        text = self.cleaned_data.get('text').strip()
        if text.isupper():
            raise ValidationError("Our AI agents are trying to sleep, don't yell")
        return text


class CreateReview(ReviewForms):
    pass


class DeleteReview(ReviewForms):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True


class EditReview(ReviewForms):
    pass
