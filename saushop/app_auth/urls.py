from django.urls import path, include
from .views import signIn, signOut, signUp_var2, signUpView

urlpatterns = [
    path("api/sign-in", signIn),
    path("api/sign-up", signUpView.as_view()),
    # path('api/sign-up', signUp_var2),
    path("api/sign-out", signOut),
]
