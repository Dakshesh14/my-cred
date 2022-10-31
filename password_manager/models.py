from django.db import models
from django.conf import settings
# utils
from utils.crypto import encrypt


class PasswordStore(models.Model):
    site_name = models.CharField(max_length=255)
    description = models.TextField()
    site_url = models.URLField(max_length=520)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    password = models.TextField()

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Password'
        verbose_name_plural = 'Passwords'

    def save(self, *args, **kwargs):
        self.password = encrypt(self.password)
        super(PasswordStore, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.site_name
