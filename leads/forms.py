from django import forms
from . models import Leads,comments,LeadFiles

class Leadsform(forms.ModelForm):
    class Meta:
        model = Leads 
        fields =('Name','email','description','priority','status',)
    
class AddCommentsform(forms.ModelForm):
    class Meta:
        model = comments
        fields =('content',)

class LeadFilesform(forms.ModelForm):
    class Meta:
        model = LeadFiles
        fields =('files',)