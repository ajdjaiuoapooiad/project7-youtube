from django import forms
from base.models import Item,User
from django.contrib.auth import get_user_model  #今使用しているUser


class ItemCreateForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=['title','text','thumbnail','movie','category','tags']
        
        
        
class UserCreateForm(forms.ModelForm):
    class Meta:
        model=get_user_model()
        fields=['username','email','password']
        
        def clean_password(self):
            password=self.cleaned_data.get('password')
            return password
        
        def save(self,commit=True):
            user=super().save(commit=False)
            user.set_password(self.cleaned_data['password'])
            
            if commit:
                user.save()
            return user
        
