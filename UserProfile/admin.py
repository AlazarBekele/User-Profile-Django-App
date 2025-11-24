from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile

# Register your models here.
admin.site.unregister(Group)

class ProfileAddUser (admin.StackedInline):
    model = Profile

class UserAdmin (admin.ModelAdmin):

    model = User
    fields = ['username', 'email', 'first_name', 'last_name']
    inlines = [ProfileAddUser]

# unregister the User
admin.site.unregister(User)

# register the User again
admin.site.register (User, UserAdmin)