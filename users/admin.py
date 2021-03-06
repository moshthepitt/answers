from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from users.models import UserProfile, UserGroup

# Define an inline admin descriptor for UserProfile model
# which acts a bit like a singleton


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'UserProfile'

# Define a new User admin


class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'customer']


class UserGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'customer', 'parent', 'manager']


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserGroup, UserGroupAdmin)
