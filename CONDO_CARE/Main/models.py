from django.db import models

class Userinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=64) 
    password = models.CharField(max_length=128)

