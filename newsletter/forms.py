from django import forms

from .models import NewsLetter


class SignUpForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
