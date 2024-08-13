from django.db import models
import os
from django.utils.crypto import get_random_string

#関数

def upload_image_to(instance,filename):  
    item_id=str(instance.id)
    return os.path.join('static/image','items',item_id,filename)

def create_id():  # urlから特定されないため   ランダムの文字列を入れる
    return get_random_string(22)
    


#models

class Category(models.Model):
    slug=models.CharField(max_length=50,primary_key=True)
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    
class Tag(models.Model):
    slug=models.CharField(max_length=50,primary_key=True)
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    


class Item(models.Model):
    id=models.CharField(default=create_id,primary_key=True,max_length=50,editable=False)
    
    uid=models.CharField('user紐付け',editable=False,max_length=50) #user紐付け
    title=models.CharField('タイトル',max_length=50)
    text=models.TextField('詳細文')
    thumbnail=models.ImageField('画像',default='',blank=True,upload_to=upload_image_to)
    movie=models.FileField('動画',upload_to='',blank=True,null=True)
    is_published=models.BooleanField('公開設定',default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True)
    tags=models.ManyToManyField(Tag,blank=True)
    
    def __str__(self):
        return self.title
    