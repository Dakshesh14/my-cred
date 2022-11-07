from rest_framework import generics, permissions
# serializers
from .serializers import PasswordStoreSerializer
# model
from password_manager.models import PasswordStore
# utils
from utils.permissions import IsOwner
from utils.crypto import decrypt


class PasswordStoreAPI(generics.ListCreateAPIView):
    serializer_class = PasswordStoreSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return PasswordStore.objects.filter(user=self.request.user).all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PasswordDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PasswordStoreSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    queryset = PasswordStore.objects.all()

    def patch(self, request, *args, **kwargs):
        password = request.data.get("password")
        if password is None:
            request.data["password"] = decrypt(
                self.get_object().password
            )
        return super().patch(request, *args, **kwargs)
