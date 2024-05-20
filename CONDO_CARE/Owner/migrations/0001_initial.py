# Generated by Django 5.0.6 on 2024-05-15 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addform1',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('occupation', models.CharField(max_length=64)),
                ('date_of_birth', models.DateField()),
                ('nationality', models.CharField(max_length=50)),
                ('home_address', models.TextField()),
                ('passport_or_nric', models.FileField(upload_to='media/')),
                ('driving_license', models.FileField(blank=True, null=True, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Addform2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('fitness_center', models.BooleanField(default=False)),
                ('swimming_pool', models.BooleanField(default=False)),
                ('parking_facilities', models.BooleanField(default=False)),
                ('children_play_area', models.BooleanField(default=False)),
                ('clubhouse', models.BooleanField(default=False)),
                ('playground', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Addform3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Contract_term', models.PositiveIntegerField(choices=[(6, '6 Months'), (12, '1 Year'), (24, '2 Years')])),
                ('floor_number', models.PositiveIntegerField()),
                ('unit_number', models.PositiveIntegerField()),
                ('security_deposit', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('refundable_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('rent_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rent_date', models.DateField()),
                ('additional_charges', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('parking_slot', models.PositiveIntegerField(blank=True, null=True)),
                ('tenant_insurance', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
    ]
