from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from portal.models import *

# Define an inline admin descriptor for Ambassador model
# which acts a bit like a singleton
class UserProfileInline(admin.StackedInline):
    model = UserExtra
    can_delete = False
    verbose_name_plural = 'userextra'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Job)
admin.site.register(Activity)
