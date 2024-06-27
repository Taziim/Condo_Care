# Generated by Django 5.0.6 on 2024-06-27 13:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('announcement_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('content', models.TextField()),
                ('post_date', models.DateField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('notification_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('content', models.TextField()),
                ('post_date', models.DateField()),
                ('audience', models.CharField(choices=[('Owner', 'Owner'), ('Tenant', 'Tenant')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
