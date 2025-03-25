from django.db import models  # ✅ Import Django's models module

class Destination(models.Model):
    url = models.URLField()  
    http_method = models.CharField(max_length=10)  
    headers = models.JSONField()  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="created_destinations")  
    updated_by = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="updated_destinations")  
