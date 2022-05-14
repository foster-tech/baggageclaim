from django.contrib import admin

from profiles.models import UserProfile, ProfilePhoto

admin.site.register(UserProfile)
admin.site.register(ProfilePhoto)
