from django import forms
from base.models import Item 


class ItemCreateForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=['title','text','thumbnail','movie','category','tags']
        
