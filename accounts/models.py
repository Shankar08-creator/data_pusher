# import uuid
# from django.db import models
# from users.models import User

# class Account(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=255)
#     app_secret_token = models.CharField(max_length=64, unique=True, editable=False)
#     website = models.URLField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     created_by = models.ForeignKey(User, related_name="created_accounts", on_delete=models.CASCADE)
#     updated_by = models.ForeignKey(User, related_name="updated_accounts", on_delete=models.CASCADE)


import uuid
from django.db import models
from django.conf import settings


class Account(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    app_secret_token = models.CharField(max_length=64, blank=True, unique=True)  # Ensure it's unique
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey('auth.User', related_name='accounts_created', on_delete=models.CASCADE)
    # updated_by = models.ForeignKey('auth.User', related_name='accounts_updated', on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='accounts_created', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='accounts_updated', on_delete=models.CASCADE)




    def save(self, *args, **kwargs):
        if not self.app_secret_token:
            self.app_secret_token = uuid.uuid4().hex  # Generates a unique token
        super().save(*args, **kwargs)
