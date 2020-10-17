# Generated by Django 2.2 on 2020-10-08 05:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201006_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_id',
            field=models.UUIDField(default=uuid.UUID('3bbdf86c-15b3-4417-8be1-906fd73e4ecb')),
        ),
        migrations.AlterField(
            model_name='withdraw',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
