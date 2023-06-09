# Generated by Django 4.1.7 on 2023-04-13 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='engine_capacity',
            field=models.IntegerField(default=0, verbose_name='Pojemność silnika (cm3)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='engine_power',
            field=models.IntegerField(default=0, verbose_name='Moc silnika (KM)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='fuel_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.carfueltype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='gear',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.cargear'),
            preserve_default=False,
        ),
    ]
