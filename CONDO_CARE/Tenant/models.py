from django.db import models
from django.core.files import File
from io import BytesIO
from PIL import Image, ImageDraw
import qrcode

class MaintenenceRequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64)
    ISSUE_TYPE_CHOICES = [
        ('Appliance', 'Appliance Repair'),
        ('Plumbing', 'Plumbing'),
        ('Electrical', 'Electrical'),
        ('House-Exterior', 'House Exterior'),
        ('Outdoors', 'Outdoors'),
        ('Other', 'Other'),
    ]
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    STATUS_CHOICES = [
        ('new', 'New'),
        ('assigned', 'Assigned'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    issue_type = models.CharField(max_length=50, choices=ISSUE_TYPE_CHOICES)
    location = models.CharField(max_length=64)
    request_datetime = models.DateTimeField()
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    photo = models.ImageField(upload_to='media/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    # status = models.CharField(max_length=20, default='pending')






















