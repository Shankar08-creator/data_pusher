from django.db import models
from django.conf import settings

class Account(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Role(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Normal User', 'Normal User'),
    )
    name = models.CharField(max_length=50, choices=ROLE_CHOICES, unique=True)

class AccountMember(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="members")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="account_memberships")
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="created_members")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="updated_members")

    class Meta:
        unique_together = ('account', 'user')  # Prevent duplicate user-account assignments
