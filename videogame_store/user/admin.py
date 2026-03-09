from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    # Fields that will be displayed in the user list
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    
    # Fields that will be displayed when editing a user
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permisos', {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(Account, AccountAdmin)