from django.db import models
from django.contrib.auth.hashers import make_password

class Userinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=64) 
    USER_TYPES = (
        ('Tenant', 'Tenant'),
        ('Owner', 'Owner'),
        ('Security', 'Security'),
        ('Management', 'Management'),
    )
    usertype = models.CharField(max_length=64, choices=USER_TYPES)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def get_usertype(self):
        return self.usertype