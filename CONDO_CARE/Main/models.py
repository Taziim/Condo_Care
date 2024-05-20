from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.
class Userinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=64) 
    USER_TYPES = (
        ('tenant', 'Tenant'),
        ('owner', 'Owner'),
        ('security', 'Security'),
        ('management', 'Management'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)