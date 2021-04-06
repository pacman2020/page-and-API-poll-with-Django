from django import forms
from django.forms import fields
from .models import Survey


class SurveyForm(forms.ModelForm):
    full_name = forms.CharField(label='Full name', required=True)
    email = forms.EmailField(label='E-mail', required=True)
    phone = forms.CharField(label='Phone', required=True)
    description = forms.CharField(label='Description', required=True)

    class Meta:
        model = Survey
        fields = (
            'full_name', 'email', 'phone', 'sex', 'language', 'description'
        )
