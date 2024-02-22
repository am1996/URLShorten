from django.db import models
from django.conf import settings
from django.utils.crypto import get_random_string
import string

class URL(models.Model):
    url = models.TextField()
    slug = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        # Ensure a unique slug is generated on every save
        if not self.slug:
            self.slug = get_random_string(length=16, allowed_chars=string.ascii_lowercase + string.ascii_uppercase + string.digits)
        super().save(*args, **kwargs)

class IP(models.Model):
    ip = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=1200)
    created_at = models.DateTimeField(auto_now_add=True)
    linked_url = models.ForeignKey(URL,on_delete=models.CASCADE)