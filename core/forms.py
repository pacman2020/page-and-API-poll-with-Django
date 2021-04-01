from django import forms
from django.forms import fields
from .models import Survey

class SurveyForm(forms.ModelForm):
    full_name = forms.CharField(label='campo full name obrigatorio', required=True)
    email = forms.EmailField(label='campo E-mail obrigatorio', required=True)
    phone = forms.CharField(label='campo phone obrigatorio', required=True)
    sex = forms.CharField(label='campo sex obrigatorio', required=True)
    language = forms.CharField(label='campo language obrigatorio', required=True)
    description = forms.CharField(label='campo description obrigatorio', required=True)
    
    class Meta:
        model = Survey
        fields = (
            'full_name', 'email', 'phone', 'sex', 'language', 'description'
        )
        
