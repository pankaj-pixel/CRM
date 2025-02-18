from django import forms
from . models import Clients,comments,ClientFiles

class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ('Name','email','description')

class AddCommentsform(forms.ModelForm):
    class Meta:
        model = comments
        fields =('content',)


class ClientFilesform(forms.ModelForm):
    class Meta:
        model = ClientFiles
        fields =('files',)        