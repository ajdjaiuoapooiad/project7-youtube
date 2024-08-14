from django.contrib import admin
from .models import Item,Category,Tag,User
from base.forms import UserCreateForm
from django.contrib.auth.admin import UserAdmin

# Register your models here
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
admin.site.register(Item)
admin.site.register(Category)

admin.site.register(Tag)

