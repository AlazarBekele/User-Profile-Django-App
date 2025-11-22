from django.contrib import admin
from django.contrib.auth.models import Group, User

# Register your models here.
admin.site.unregister(Group)

class UserAdmin (admin.ModelAdmin):

    model = User
    fields = ['username', 'email', 'first_name', 'last_name']

# unregister the User
admin.site.unregister(User)

# register the User again
admin.site.register (User, UserAdmin)