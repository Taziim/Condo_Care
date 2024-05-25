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


class FacilityBooking(models.Model):
    id = models.BigAutoField(primary_key=True)
    booker_name = models.CharField(max_length=100)
    floor_number = models.IntegerField()
    unit_number = models.IntegerField()
    facility = models.CharField(max_length=50, choices=[
        ('common-room', 'Common Room'),
        ('hall-room', 'Hall Room'),
        ('swimming-pool', 'Swimming Pool'),
        ('bbq-area', 'BBQ Area'),
        ('rooftop-terrace', 'Rooftop Terrace'),
        ('sports-facilities', 'Sports Facilities'),
    ])
    booking_date = models.DateField()
    booking_time = models.CharField(max_length=20, choices=[
        ('9:00 am To 10:00 am', '9:00 am To 10:00 am'),
        ('10:00 am To 11:00 am', '10:00 am To 11:00 am'),
        ('11:00 am To 12:00 pm', '11:00 am To 12:00 pm'),
        ('12:00 pm To 1:00 pm', '12:00 pm To 1:00 pm'),
        ('1:00 pm To 2:00 pm', '1:00 pm To 2:00 pm'),
        ('2:00 pm To 3:00 pm', '2:00 pm To 3:00 pm'),
        ('3:00 pm To 4:00 pm', '3:00 pm To 4:00 pm'),
        ('4:00 pm To 5:00 pm', '4:00 pm To 5:00 pm'),
        ('5:00 pm To 6:00 pm', '5:00 pm To 6:00 pm'),
        ('6:00 pm To 7:00 pm', '6:00 pm To 7:00 pm'),
        ('7:00 pm To 8:00 pm', '7:00 pm To 8:00 pm'),
        ('8:00 pm To 9:00 pm', '8:00 pm To 9:00 pm'),
    ])
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approve', 'Approved'),
        ('rejected', 'Rejected'),
    ] 
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    attendees = models.IntegerField()
    additional_notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class MakeComplaint(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    floor_number = models.PositiveIntegerField()
    unit_number = models.PositiveIntegerField()
    category = models.CharField(
        max_length=20,
        choices=[
            ('maintenance', 'Maintenance'),
            ('noise', 'Noise'),
            ('security', 'Security'),
            ('tenant', 'Tenant'),
            ('amenities', 'Amenities'),
            ('other', 'Other'),
        ],
    )
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('resolved', 'Resolved'),
    ] 
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open')
    date = models.DateField()
    description = models.TextField()
    attachment = models.FileField(upload_to='media/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


    






















