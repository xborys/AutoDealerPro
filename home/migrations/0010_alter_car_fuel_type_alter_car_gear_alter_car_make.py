# Generated by Django 4.1.7 on 2023-04-18 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_client_opinion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(choices=[('benzyna', 'Benzyna'), ('diesel', 'Diesel'), ('hybryda', 'Hybryda'), ('elektryczny', 'Elektryczny'), ('lpg', 'LPG')], max_length=50, verbose_name='Rodzaj paliwa'),
        ),
        migrations.AlterField(
            model_name='car',
            name='gear',
            field=models.CharField(choices=[('manual', 'Manualna'), ('automat', 'Automatyczna')], max_length=50, verbose_name='Skrzynia biegów'),
        ),
        migrations.AlterField(
            model_name='car',
            name='make',
            field=models.CharField(choices=[('audi', 'Audi'), ('bmw', 'BMW'), ('ford', 'Ford'), ('honda', 'Honda'), ('hyundai', 'Hyundai'), ('kia', 'Kia'), ('mazda', 'Mazda'), ('mercedes_benz', 'Mercedes-Benz'), ('nissan', 'Nissan'), ('opel', 'Opel'), ('renault', 'Renault'), ('skoda', 'Skoda'), ('toyota', 'Toyota'), ('volkswagen', 'Volkswagen')], max_length=50, verbose_name='Marka'),
        ),
    ]
