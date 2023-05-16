# Generated by Django 4.1.7 on 2023-04-19 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_car_fuel_type_alter_car_gear_alter_car_make'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='gear',
            field=models.CharField(choices=[('Manualna', 'Manualna'), ('Automatyczna', 'Automatyczna')], max_length=50, verbose_name='Skrzynia biegów'),
        ),
        migrations.AlterField(
            model_name='car',
            name='make',
            field=models.CharField(choices=[('Audi', 'Audi'), ('BMW', 'BMW'), ('Ford', 'Ford'), ('Honda', 'Honda'), ('Hyundai', 'Hyundai'), ('Kia', 'Kia'), ('Mazda', 'Mazda'), ('Mercedes-Benz', 'Mercedes-Benz'), ('Nissan', 'Nissan'), ('Opel', 'Opel'), ('Renault', 'Renault'), ('Skoda', 'Skoda'), ('Toyota', 'Toyota'), ('Tesla', 'Tesla'), ('Volkswagen', 'Volkswagen')], max_length=50, verbose_name='Marka'),
        ),
    ]