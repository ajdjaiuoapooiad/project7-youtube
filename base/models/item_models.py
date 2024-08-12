from django.db import models


class Category(models.Model):
    slug=
    name=
    def __str__(self):
        return self.name
    
    
class Tag(models.Model):
    slug=
    name=
    def __str__(self):
        return self.name
    


class Item(models.Model):
    id=
    uid=
    title=models.CharField('タイトル',max_length=50)
    text=models.TextField('詳細文')
    thumbnail=models.ImageField('画像',upload_to='')
    movie=models.FileField('動画',upload_to='')
    is_published=
    created_at=
    updated_at=
    
    category=
    tags=
    
    def __str__(self):
        return self.title
    