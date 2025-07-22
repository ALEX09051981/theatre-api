from django.urls import path

from user.views import CreateUserView, CreateTokenView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="user-register"),
    path("login/", CreateTokenView.as_view(), name="token"),
]
