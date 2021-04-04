# Generated by Django 2.2 on 2021-04-04 12:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210305_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='select_currency',
            field=models.CharField(blank=True, choices=[('Dollars($)', 'Dollars($)'), ('Pounds()', 'Pounds()'), ('Euros()', 'Euros()')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_id',
            field=models.UUIDField(default=uuid.UUID('c806ffa4-f5ab-4b3b-839a-1071d75d0a41')),
        ),
    ]
