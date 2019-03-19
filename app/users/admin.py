from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth import admin as auth_admin

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    fieldsets = (('User',
                  {"fields": (
                      'username', 'nickname', 'first_name', 'last_name', 'email', 'profile_image'
                  )}),)
    search_fields = ['username']
