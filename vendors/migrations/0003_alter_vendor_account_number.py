# Generated by Django 5.0.3 on 2024-04-07 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0002_alter_vendor_account_type_alter_vendor_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='account_number',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
