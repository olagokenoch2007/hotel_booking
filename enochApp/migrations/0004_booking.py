# Generated by Django 5.1.6 on 2025-03-05 10:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enochApp', '0003_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('adult', models.PositiveIntegerField()),
                ('child', models.PositiveIntegerField(blank=True, null=True)),
                ('special_request', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('room', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='enochApp.apartment')),
            ],
        ),
    ]
