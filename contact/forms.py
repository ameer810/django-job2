from django import forms
from .models import Info
class Infoform(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['phone_number', 'email','place']