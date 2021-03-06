# Generated by Django 2.2 on 2021-03-01 04:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201122_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='latesttransactions',
            name='status',
            field=models.CharField(choices=[('Confirmed', 'Confirmed'), ('Unconfirmed', 'Unconfirmed'), ('Canceled', 'Canceled')], default='', max_length=18),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_id',
            field=models.UUIDField(default=uuid.UUID('d1dd30e1-2d1d-4bb3-82dd-cb12f844361c')),
        ),
        migrations.CreateModel(
            name='WithdrawalVerification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verification_method', models.CharField(choices=[('Drivers License', 'Drivers License'), ('US Passort/Card', 'US Passort/Card'), ('US Military Card', 'US Military Card'), ('Military Dependents Card', 'Military Dependents Card'), ('Permananet Resident Card', 'Permananet Resident Card'), ('Certificate of Citizenship', 'Certificate of Citizenship'), ('Certificate of Naturalization', 'Certificate of Naturalization'), ('Employment Authorization Document', 'Employment Authorization Document'), ('Foreign Passport', 'Foreign Passport')], default='', max_length=30)),
                ('upload_document', models.FileField(upload_to='doc/withdraw/documents')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
