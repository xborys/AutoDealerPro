# Generated by Django 4.1.7 on 2023-04-24 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_car_doors_alter_car_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='availability',
            field=models.BooleanField(default=False, verbose_name='Dostępność'),
        ),
    ]
