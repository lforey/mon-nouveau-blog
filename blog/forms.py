from django import forms
 
from .models import Player
 
class MoveForm(forms.ModelForm):
 
    class Meta:
        model = Player
        fields = ('activity',)