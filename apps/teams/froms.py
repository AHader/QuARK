from django import forms

from .models import Transfer


class JoinForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = ('from_ngb','reason',)
        labels = {
            "from_ngb": "Are you an international transfer, please state here otherwise click next!",
        }


class TransferForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = ('reason',)
