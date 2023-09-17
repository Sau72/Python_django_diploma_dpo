from django.contrib import admin
from .models import Profile, ImageProfile


@admin.register(ImageProfile)
class ImageProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "src", "alt"]


@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "fullName", "email", "phone", "avatar"]
