from django.db import models
from django.contrib.auth.models import User


def avatar_preview_directory_path(instance: "ImageProfile", filename: str) -> str:
    return "profile/users/{filename}".format(
        filename=filename,
    )


class ImageProfile(models.Model):
    src = models.ImageField(
        null=True,
        blank=True,
        upload_to=avatar_preview_directory_path,
        verbose_name="аватар",
    )
    alt = models.CharField(max_length=30, verbose_name="инфо картинки")

    class Meta:
        verbose_name = "image avatar"
        verbose_name_plural = "images avatar"

    def __str__(self):
        return self.alt


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=30, verbose_name="ФИО")
    email = models.CharField(
        max_length=30, verbose_name="эл. почта", null=True, blank=True
    )
    phone = models.CharField(
        max_length=30, verbose_name="телефон", null=True, blank=True
    )
    avatar = models.ForeignKey(
        ImageProfile, on_delete=models.PROTECT, null=True, blank=True
    )

    class Meta:
        verbose_name = "user profile"
        verbose_name_plural = "user profile"

    def __str__(self):
        return self.fullName
