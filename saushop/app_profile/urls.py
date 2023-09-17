from django.urls import path, include
from api import views
from .views import (
    ProfileView,
    ProfileViewUpdate,
    ProfilePasswordViewUpdate,
    ChangeAvatarView,
)

# from rest_framework.routers import DefaultRouter

# routers = DefaultRouter()
# routers.register("avatar", ChangeAvatarView)

app_name = "app_profile"

urlpatterns = [
    path("api/profile/", ProfileView.as_view()),
    path("api/profile/password", ProfilePasswordViewUpdate.as_view()),
    path("api/profile", ProfileViewUpdate.as_view()),
    # path('api/profile/', include(routers.urls))
    path("api/profile/avatar", ChangeAvatarView.as_view()),
]
