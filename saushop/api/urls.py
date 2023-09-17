from django.urls import path, include
from api import views

urlpatterns = [
    path("profile", views.profile),
    path("categories", views.categories),
    # path('catalog', views.catalog),
    # path('api-auth/', include('rest_framework.urls')),
]
