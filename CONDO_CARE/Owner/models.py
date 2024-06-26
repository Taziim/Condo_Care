from django.db import models


class Addform1(models.Model):
     id = models.BigAutoField(primary_key=True)
     full_name = models.CharField(max_length=64)
     email = models.EmailField(unique=True)
     phone_number = models.CharField(max_length=20)
     occupation = models.CharField(max_length=64)
     date_of_birth = models.DateField()
     nationality = models.CharField(max_length=50)
     home_address = models.TextField()
     passport_or_nric = models.FileField(upload_to='media/', null=True, blank=True)
     driving_license = models.FileField(upload_to='media/', null=True, blank=True)

class Addform2(models.Model):
    fitness_center = models.BooleanField(default=False)
    swimming_pool = models.BooleanField(default=False)
    parking_facilities = models.BooleanField(default=False)
    children_play_area = models.BooleanField(default=False)
    clubhouse = models.BooleanField(default=False)
    playground = models.BooleanField(default=False)

class Addform3(models.Model):
    CONTRACT_CHOICES = [
        (6, '6 Months'),
        (12, '1 Year'),
        (24, '2 Years'),
    ]
    Contract_term = models.PositiveIntegerField(choices=CONTRACT_CHOICES)
    floor_number = models.PositiveIntegerField()
    unit_number = models.PositiveIntegerField()
    security_deposit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    refundable_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rent_fee = models.DecimalField(max_digits=10, decimal_places=2)
    rent_date = models.DateField()
    additional_charges = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    parking_slot = models.PositiveIntegerField(null=True, blank=True)
    tenant_insurance = models.CharField(max_length=64, null=True, blank=True)
    



