# Generated by Django 3.0.7 on 2020-07-16 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200716_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(max_length=20),
        ),
    ]
