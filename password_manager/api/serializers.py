from rest_framework import serializers
# models
from password_manager.models import PasswordStore
# utils
from utils.crypto import decrypt


class PasswordStoreSerializer(serializers.ModelSerializer):

    dec_password = serializers.SerializerMethodField()

    class Meta:
        model = PasswordStore
        fields = (
            'id',
            'title',
            'description',
            'site_username',
            'site_url',
            'dec_password',
            'password',
            'created_at',
            'updated_at',
            'meta',
        )
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def get_dec_password(self, obj):
        return decrypt(obj.password)
