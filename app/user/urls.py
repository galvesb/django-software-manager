from django.urls import path

from .views import RegisterUser, Login

urlpatterns = [
    path("user/register", RegisterUser.as_view()),
    path("auth/login", Login.as_view()),
]
