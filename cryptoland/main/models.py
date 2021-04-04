from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from django.utils.translation import ugettext_lazy as _

''' custom user stuff '''
# timezone for custom user model
from django.utils import timezone

# importing uuid for custom username ids
import uuid

# use this instead of User
from django.contrib.auth import settings

''' 
for phone field
'''
from phonenumber_field.modelfields import PhoneNumberField


'''
    creating custom user
'''
# CUSTOM user first design

class CustomUserManager(BaseUserManager):
    ''' custom user model manager wher email is the unique identifiers for authentication instead of usernames '''

    def _create_user(self, email, password,is_staff, is_superuser, **extra_fields):
        ''' create and save a User with the given email and password '''
        if not email:
            raise ValueError(_('The email must be set'))
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)
    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email  

"""
    Registration  models
    
"""

# profile

plans = (
    ('Bronze', 'Bronze'),
    ('Silver', 'Silver'),
    ('Gold', 'Gold'),
    ('Platinum', 'Platinum')
)
class Profile(models.Model):
    currency = (
        ('Dollars($)', 'Dollars($)'),
        ('Pounds()', 'Pounds()'),
        ('Euros()', 'Euros()'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=23, default='', blank=True)
    last_name = models.CharField(max_length=23, default='', blank=True)
    phone_number = PhoneNumberField(blank=True, help_text='Contact Phone Number')
    street_address = models.CharField(max_length=150, default='', blank=True)
    city =  models.CharField(max_length = 100, default=False, blank=True)
    state = models.CharField(max_length=30, default= '', blank=True)
    postal_or_zip_code = models.CharField(max_length=6, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    country = CountryField(blank_label='(select country)', blank=True, null=True)
    select_plan = models.CharField(max_length=40, choices=plans)
    select_currency = models.CharField(max_length=200, choices=currency, blank=True, null=True)
    def __str__(self):
        return self.first_name
        
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

'''
    Dashboard  models
'''
# balance
class Balance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

# contact
class Contact(models.Model):
    topic = models.CharField(max_length=150, default='')
    name = models.CharField(max_length=150, default='')
    email = models.EmailField(max_length=50, default='')
    message = models.TextField()

# invested amount
class InvestedAmount(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

# forex signals 
class Signals(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

# Notifications
class Notification(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    details = models.CharField(max_length=40)
    amount = models.PositiveIntegerField()

# withdrawal
class Withdraw(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    wallet_address = models.CharField(max_length=40, default='')
    message = models.CharField(max_length=60, default= '', blank=True, null=True)
    withdraw_status = models.BooleanField(default=False, blank=True, null=True)

class WithdrawalVerification(models.Model):
    documents = (
        ('Drivers License', 'Drivers License'),
        ('US Passort/Card', 'US Passort/Card'),
        ('US Military Card', 'US Military Card'),
        ('Military Dependents Card', 'Military Dependents Card'),
        ('Permananet Resident Card', 'Permananet Resident Card'),
        ('Certificate of Citizenship', 'Certificate of Citizenship'),
        ('Certificate of Naturalization', 'Certificate of Naturalization'),
        ('Employment Authorization Document', 'Employment Authorization Document'),
        ('Foreign Passport', 'Foreign Passport')
        
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    verification_method= models.CharField(max_length=30, default='', choices=documents)
    upload_document = models.FileField(upload_to='doc/withdraw/documents', blank=False, null=False)

# bitcoin balance
class BTCbalance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=11, decimal_places=11)

# daily Investments
class DailyInvestments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    amount = models.PositiveIntegerField()

documents = (
    ('Drivers License', 'Drivers License'),
    ('US Passort/Card', 'US Passort/Card'),
    ('US Military Card', 'US Military Card'),
    ('Military Dependents Card', 'Military Dependents Card'),
    ('Permananet Resident Card', 'Permananet Resident Card'),
    ('Certificate of Citizenship', 'Certificate of Citizenship'),
    ('Certificate of Naturalization', 'Certificate of Naturalization'),
    ('Employment Authorization Document', 'Employment Authorization Document'),
    ('Foreign Passport', 'Foreign Passport')
    
)
# verification documents
class VerificationDocument(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=100, choices=documents)
    front_document = models.FileField(upload_to='doc/front_page/', blank=False, null=False)
    back_document = models.FileField(upload_to='doc/back_page/', blank=False, null=False)
    verified = models.BooleanField(default=False, blank=True)

class Transaction(models.Model):
    types = (
        ('deposit', 'deposit'), 
        ('withdraw', 'withdraw'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    transaction_id = models.UUIDField(default=uuid.uuid4())
    amount = models.IntegerField()
    type = models.CharField(max_length=30, choices=types)

class LatestTransactions(models.Model):
    preference = (
        ('High' ,'High'),
        ('Medium', 'Medium'),
        ('Low' ,'Low'),
    )

    status = (
        ('Confirmed', 'Confirmed'),
        ('Unconfirmed', 'Unconfirmed'),
        ('Canceled', 'Canceled'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    btc = models.CharField(max_length=30, default='0.00')
    time = models.DateTimeField(auto_now=True)
    miner_preference = models.CharField(max_length=20, choices=preference)
    status = models.CharField(max_length=18,default='', choices=status )