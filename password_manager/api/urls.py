from django.urls import path

from .api import PasswordStoreAPI, PasswordDetailAPI

urlpatterns = [
    path('passwords', PasswordStoreAPI.as_view(), name="password-list"),
    path('passwords/<int:pk>', PasswordDetailAPI.as_view(), name="password-detail")
]
