from django.contrib import admin
from base.models import Item,Category,Tag,User,Profile
from base.forms import UserCreateForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

# Register your models here

#下記の二つがアイテムモデルにタグモデルを表示するため
class TagInline(admin.TabularInline):
    model = Item.tags.through
 
 
class ItemAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    exclude = ['tags']
    
    
    
    
    
class ProfileInline(admin.StackedInline):
    model=Profile
    can_delete=False


class CustomAdmin(UserAdmin):
    fieldsets=(
        (None, {'fields':('username','email','password')}),
        (None,{'fields':('is_active','is_admin')}),
    )
    list_display=('username','email','is_active')
    list_filter=()
    ordering=()
    filter_horizontal=()
    
    add_fieldsets=(
        (None,{'fields':('username','email','is_active')}),
    )
    add_form=UserCreateForm
    #  inlines=(ProfileInline,) 




admin.site.register(User,CustomAdmin)
admin.site.register(Item,ItemAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.unregister(Group)

