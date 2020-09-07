# Generated by Django 3.0.7 on 2020-07-16 10:17

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200630_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fax_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
