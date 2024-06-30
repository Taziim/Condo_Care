from django.db import models

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

