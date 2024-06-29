# Generated by Django 5.0.6 on 2024-06-29 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FacilityBooking',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('booker_name', models.CharField(max_length=100)),
                ('floor_number', models.IntegerField()),
                ('unit_number', models.IntegerField()),
                ('facility', models.CharField(choices=[('common-room', 'Common Room'), ('hall-room', 'Hall Room'), ('swimming-pool', 'Swimming Pool'), ('bbq-area', 'BBQ Area'), ('rooftop-terrace', 'Rooftop Terrace'), ('sports-facilities', 'Sports Facilities')], max_length=50)),
                ('booking_date', models.DateField()),
                ('booking_time', models.CharField(choices=[('9:00 am To 10:00 am', '9:00 am To 10:00 am'), ('10:00 am To 11:00 am', '10:00 am To 11:00 am'), ('11:00 am To 12:00 pm', '11:00 am To 12:00 pm'), ('12:00 pm To 1:00 pm', '12:00 pm To 1:00 pm'), ('1:00 pm To 2:00 pm', '1:00 pm To 2:00 pm'), ('2:00 pm To 3:00 pm', '2:00 pm To 3:00 pm'), ('3:00 pm To 4:00 pm', '3:00 pm To 4:00 pm'), ('4:00 pm To 5:00 pm', '4:00 pm To 5:00 pm'), ('5:00 pm To 6:00 pm', '5:00 pm To 6:00 pm'), ('6:00 pm To 7:00 pm', '6:00 pm To 7:00 pm'), ('7:00 pm To 8:00 pm', '7:00 pm To 8:00 pm'), ('8:00 pm To 9:00 pm', '8:00 pm To 9:00 pm')], max_length=20)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approve', 'Approved'), ('rejected', 'Rejected')], default='Pending', max_length=20)),
                ('attendees', models.IntegerField()),
                ('additional_notes', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MaintenenceRequest',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('issue_type', models.CharField(choices=[('Appliance', 'Appliance Repair'), ('Plumbing', 'Plumbing'), ('Electrical', 'Electrical'), ('House-Exterior', 'House Exterior'), ('Outdoors', 'Outdoors'), ('Other', 'Other')], max_length=50)),
                ('location', models.CharField(max_length=64)),
                ('request_datetime', models.DateTimeField()),
                ('description', models.TextField()),
                ('priority', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], max_length=10)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('status', models.CharField(choices=[('new', 'New'), ('assigned', 'Assigned'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='new', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MakeComplaint',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('floor_number', models.PositiveIntegerField()),
                ('unit_number', models.PositiveIntegerField()),
                ('category', models.CharField(choices=[('maintenance', 'Maintenance'), ('noise', 'Noise'), ('security', 'Security'), ('tenant', 'Tenant'), ('amenities', 'Amenities'), ('other', 'Other')], max_length=20)),
                ('status', models.CharField(choices=[('open', 'Open'), ('resolved', 'Resolved')], default='Open', max_length=20)),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('attachment', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TenantPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_month', models.IntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')])),
                ('rent_amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('electricity_amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('water_amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('payment_method', models.CharField(choices=[('Online_Payment', 'Online Payment'), ('Manual_Payment', 'Manual Payment')], max_length=15)),
                ('payment_date', models.DateField(auto_now_add=True)),
                ('proof_of_rent', models.FileField(blank=True, null=True, upload_to='media/')),
                ('proof_of_electricity', models.FileField(blank=True, null=True, upload_to='media/')),
                ('proof_of_water', models.FileField(blank=True, null=True, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='VisitorRegistrationTenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_name', models.CharField(max_length=64)),
                ('visitor_contact', models.CharField(max_length=20)),
                ('floor_number', models.PositiveIntegerField()),
                ('unit_number', models.PositiveIntegerField()),
                ('reason_to_visit', models.TextField()),
                ('datetime_local', models.DateTimeField()),
            ],
        ),
    ]
