# Generated by Django 4.1.7 on 2023-03-24 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_car_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Imię i nazwisko / Nazwa firmy')),
                ('pesel', models.IntegerField(blank=True, null=True, verbose_name='PESEL')),
                ('nip', models.IntegerField(blank=True, null=True, verbose_name='NIP')),
                ('adress', models.CharField(max_length=100, verbose_name='Adres')),
                ('city', models.CharField(max_length=50, verbose_name='Miasto')),
                ('zip', models.IntegerField(verbose_name='Kod pocztowy')),
                ('phone', models.IntegerField(verbose_name='Telefon')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Imię i nazwisko')),
                ('adress', models.CharField(max_length=100, verbose_name='Adres')),
                ('city', models.CharField(max_length=50, verbose_name='Miasto')),
                ('zip', models.IntegerField(verbose_name='Kod pocztowy')),
                ('phone', models.IntegerField(verbose_name='Telefon')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('position', models.CharField(max_length=50, verbose_name='Stanowisko')),
                ('hire_date', models.DateField(verbose_name='Data zatrudnienia')),
                ('fire_date', models.DateField(blank=True, null=True, verbose_name='Data zwolnienia')),
            ],
        ),
        migrations.AlterField(
            model_name='car',
            name='description',
            field=models.TextField(verbose_name='Opis'),
        ),
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Zdjęcia'),
        ),
        migrations.AlterField(
            model_name='car',
            name='make',
            field=models.CharField(max_length=50, verbose_name='Marka'),
        ),
        migrations.AlterField(
            model_name='car',
            name='mileage',
            field=models.IntegerField(verbose_name='Przebieg (km)'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=50, verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.IntegerField(verbose_name='Cena (PLN)'),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(verbose_name='Rok produkcji'),
        ),
    ]