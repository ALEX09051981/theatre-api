from django.urls import path

from user.views import CreateUserView, CreateTokenView, ManageUserView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="user-register"),
    path("login/", CreateTokenView.as_view(), name="token"),
    path("me/", ManageUserView.as_view(), name="manage"),
]
