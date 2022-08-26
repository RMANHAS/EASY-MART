from django.contrib import admin
from user_profile.models import UserProfile
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','mobile']
    search_fields = ['mobile']


admin.site.register(UserProfile,UserProfileAdmin)