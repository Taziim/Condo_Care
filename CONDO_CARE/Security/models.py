from django.db import models
from django.core.files import File


class VisitorRegistration(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64)
    tenant_name = models.CharField(max_length=64)
    floor_number = models.IntegerField()
    unit_number = models.IntegerField()
    phone_number = models.CharField(max_length=64)
    home_address  = models.TextField()
    reason_to_visit  = models.TextField()
    TOWER_CHOICES = [
        ('Tower 1', 'Tower 1'),
        ('Tower 2', 'Tower 2'),
        ('Tower 3', 'Tower 3'),
        ('others', 'Others'),
    ]

    tower_select = models.CharField(choices=TOWER_CHOICES)
    datetime_local = models.DateTimeField()


class Emergency(models.Model):
    id = models.BigAutoField(primary_key=True)
    EMERGENCY_TYPES = [
        ('fire', 'Fire'),
        ('medical', 'Medical Emergency'),
        ('security', 'Security Threat'),
    ]

    emergency_type = models.CharField(max_length=20, choices=EMERGENCY_TYPES)
    emergency_details = models.TextField()
    notify_email = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)


from django import forms


from django.db import models
from django.utils import timezone

class IncidentReport(models.Model):
    INCIDENT_TYPES = [
        ('Theft', 'Theft'),
        ('Vandalism', 'Vandalism'),
        ('Suspicious_Activity', 'Suspicious Activity'),
        ('Parking_Violation', 'Parking Violation'),
        ('Others', 'Others'),
    ]

    incidenttype = models.CharField(max_length=60, choices=INCIDENT_TYPES)
    description = models.TextField()
    location = models.CharField(max_length=155)
    datetimereported = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to='media/', null=True, blank=True)




















# class Qrcode(models.Model):
#     name = models.CharField(max_length=30)
#     qr_code = models.ImageField(upload_to='media/', blank=True)

#     def save(self, *args, **kwargs):
#         # Create QR code image
#         qrcodeimg = qrcode.make(self.name)
#         canvas = Image.new('RGB', (290, 290), 'white')
#         canvas.paste(qrcodeimg)
        
#         # Save the image to a BytesIO buffer
#         buffer = BytesIO()
#         canvas.save(buffer, 'PNG')
#         fname = f'qr_code-{self.name}.png'
#         self.qr_code.save(fname, File(buffer), save=False)
#         buffer.close()
#         super().save(*args, **kwargs)

