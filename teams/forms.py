from django import forms
from . models import Team

class Teamsform(forms.ModelForm):
    class Meta:
        model = Team 
        fields =('Name',)
    