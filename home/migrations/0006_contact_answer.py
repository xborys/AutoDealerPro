# Generated by Django 4.1.7 on 2023-04-14 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_yes_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='answer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.yes_no'),
        ),
    ]
