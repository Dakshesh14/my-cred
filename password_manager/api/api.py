from rest_framework import generics, permissions
# serializers
from .serializers import PasswordStoreSerializer
# model
from password_manager.models import PasswordStore
# utils
from utils.permissions import IsOwner


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
