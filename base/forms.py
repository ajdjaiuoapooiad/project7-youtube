from django import forms
from base.models import Item,User


class ItemCreateForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=['title','text','thumbnail','movie','category','tags']
        
class AccountCreateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']