# Generated by Django 2.2 on 2021-04-12 15:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210406_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_id',
            field=models.UUIDField(default=uuid.UUID('16dca55f-ff8e-4776-9b04-16a9d81f1072')),
        ),
    ]
