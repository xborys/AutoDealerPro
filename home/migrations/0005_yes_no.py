# Generated by Django 4.1.7 on 2023-04-14 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_car_make'),
    ]

    operations = [
        migrations.CreateModel(
            name='yes_no',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yes_no', models.CharField(max_length=3, verbose_name='Wartość')),
            ],
        ),
    ]
