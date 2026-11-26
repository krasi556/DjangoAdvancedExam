from django import forms

from members.models import Endorsement


class EndorsementForm(forms.ModelForm):
    class Meta:
        model = Endorsement
        fields = ['amount']