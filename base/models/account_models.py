#ここからコピーした 
   
   
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
#kokokara 追記
from base.models import create_id
from django.dispatch import receiver
from django.db.models.signals import post_save
import os



##kokokara 関数
def upload_image_to(instance,filename):  
    item_id=str(instance.id)
    return os.path.join('static/image','items',item_id,filename)



##ここからモデル
class MyUserManager(BaseUserManager):
    def create_user(self,username, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id=models.CharField(default=create_id,max_length=50,primary_key=True)
    username=models.CharField(max_length=50,default='名無し',unique=True,blank=True)
    #kokokara copy
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD='email'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin 
    
    
    
class Profile(models.Model):  #追記　モデル全て
    #Userとの紐付け
    user=models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE) 
    
    ##追記  
    userimage=models.ImageField('アイコン画像',default='',blank=True,upload_to=upload_image_to)
    
    
    name=models.CharField(default='',blank=True,max_length=30)
    zipcode=models.CharField(default='',blank=True,max_length=8)
    #住所
    prefecture=models.CharField(default='',blank=True,max_length=50)
    city=models.CharField(default='',blank=True,max_length=50)
    address1=models.CharField(default='',blank=True,max_length=50)
    address2=models.CharField(default='',blank=True,max_length=50)
    tel=models.CharField(default='',blank=True,max_length=15)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
# OneToOneFieldを同時に作成
@receiver(post_save, sender=User)
def create_onetoone(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])
    
    

    
    
