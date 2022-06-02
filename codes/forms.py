from django import forms
from .models import Code

class Codeform(forms.ModelForm):
    number = forms.CharField(label='Code', help_text='enter the code which is just sent to your number')
    class Meta:
        model=Code 
        fields=('number',)