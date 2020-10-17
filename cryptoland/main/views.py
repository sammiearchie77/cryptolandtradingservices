from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import login as auth_login

# import user settings
from django.contrib.auth import get_user_model

from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm, ProfileForm, WithdrawalForm, VerificationDocumentForm, ContactForm

# models
from .models import Balance, Signals, InvestedAmount, BTCbalance, Profile, DailyInvestments, VerificationDocument
from .models import CustomUser, Transaction, Withdraw
from django.db.models import Sum

# password reset 
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# time, dateteime
# import time
import datetime


''' views with no logic  '''

# homepage
def index(request):
    return render(request, 'main/index.html')

# About us page
def about(request):
    return render(request, 'main/about.html')

# contact page
# send mail thing
from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data.get('topic')
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            send_mail(topic,message,'support@cryptolifeinvestment.com', [email,])

            return redirect('main:home')
        else:
            print('form invalid')

    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'main/contact.html', context)

# Privacy Policy
def privacy_policy(request):
    return render(request, 'main/privacy-policy.html')

# payment policy
def payment_policy(request):
    return render(request, 'main/payment-policy.html')

# terms and conditions
def terms_and_condition(request):
    return render(request,'main/terms-and-conditions.html')

def safety_of_funds(request):
    return render(request, 'main/safety-of-funds.html')
     
''' views with logic '''

'''             dashboard things             '''

# dashboard homepage / trading center
@login_required(login_url='login')
def dashboard(request):
    user = request.user

    # dashboard info from database
    balance = Balance.objects.filter(user=user).aggregate(amount=Sum('amount'))
    signals_amount = Signals.objects.filter(user=user).aggregate(amount=Sum('amount'))
    withdraw = Withdraw.objects.filter(user=user).aggregate(amount=Sum('amount'))
    invested = InvestedAmount.objects.filter(user=user).aggregate(amount=Sum('amount'))
    btc_balance = BTCbalance.objects.filter(user=user).aggregate(amount=Sum('amount'))
    daily_investments = DailyInvestments.objects.filter(user=user).aggregate(amount=Sum('amount'))
    transaction_details = Transaction.objects.filter(user=user)

    # id verification logic
    if request.method == 'POST':
        verification_form = VerificationDocumentForm(request.POST,request.FILES)
        if verification_form.is_valid():
            # verification model 
            ver_model = VerificationDocument
            
            # collect form data
            document_type = verification_form.cleaned_data.get('document_type')
            front_document = verification_form.cleaned_data.get('front_document')
            back_document = verification_form.cleaned_data.get('back_document')

            # pass form data to the model
            ver_model.objects.create(
                user = request.user,
                document_type=document_type,
                front_document=front_document,
                back_document=back_document
            )
            return redirect('main:dashboard')  
        else:
            print(verification_form.errors)
    else:
        verification_form = VerificationDocumentForm()

    context = {
        'balance': balance, 
        'signals': signals_amount, 
        'invested': invested,
        'btc_balance': btc_balance,
        'daily_investments': daily_investments, 
        'verification_form': verification_form, 
        # 'transaction':transaction_details, 
        'withdraw': withdraw
    }
    return render(request, 'main/dashboard.html', context)

# fund account
from django.contrib import messages
@login_required(login_url='/accounts/login')
def fund_account(request):
    user = request.user
    # dashboard info from database
    balance = Balance.objects.filter(user=user).aggregate(amount=Sum('amount'))
    signals_amount = Signals.objects.filter(user=user).aggregate(amount=Sum('amount'))
    withdraw = Withdraw.objects.filter(user=user).aggregate(amount=Sum('amount'))
    invested = InvestedAmount.objects.filter(user=user).aggregate(amount=Sum('amount'))
    btc_balance = BTCbalance.objects.filter(user=user).aggregate(amount=Sum('amount'))
    daily_investments = DailyInvestments.objects.filter(user=user).aggregate(amount=Sum('amount'))
    transaction_details = Transaction.objects.filter(user=user)

    context = {
        'balance': balance, 
        'invested': invested,
        'withdraw': withdraw
    }
    return render(request, 'main/fund-account.html', context)

# transactions view 
def trading_history(request):
    return render(request, 'main/trading-history.html')

# withdrawal fn
from django.contrib.auth.hashers import check_password

@login_required(login_url='/accounts/login')
def withdraw_funds(request): 
    User = get_user_model()
    user = request.user
    user_balance = Balance.objects.filter(user=user)
    balance = user_balance.aggregate(amount=Sum('amount'))
    print(user_balance)
    userPassword = request.user.password
    if request.method == 'POST':     
        form = WithdrawalForm(request.POST)
        
        if form.is_valid():
            form.save(commit=False)
            amount = form.cleaned_data.get('amount')
            wallet_address = form.cleaned_data.get('wallet_address')
            password = form.cleaned_data.get('password')
            match_password = check_password(password, userPassword)
            # messages.success(request, 'Withdraw Successful')
            user = CustomUser.objects.get(user_id=request.user.user_id)
            if match_password:
                # form.save()
                Withdraw.objects.create(
                    user= user, 
                    amount=amount, 
                    wallet_address=wallet_address
                )
                return redirect('main:dashboard')
            else:
                print('problem with matching password')
        else: 
            print('error')
    else:
        form = WithdrawalForm()

    context = {
        'form': form,
        'balance': balance,
    }

    return render(request, 'main/withdraw-funds.html', context )

# document verification
from django.contrib.auth import get_user_model
from .models import CustomUser

@login_required(login_url='login')
def id_verification(request):
    if request.method == 'POST':
        verification_form = VerificationDocumentForm(request.POST,request.FILES)
        if verification_form.is_valid():
            # verification model
            ver_model = VerificationDocument

            # collect form data
            document_type = verification_form.cleaned_data.get('document_type')
            front_document = verification_form.cleaned_data.get('front_document')
            back_document = verification_form.cleaned_data.get('back_document')
            ver_model.objects.create(
                user = request.user,
                document_type=document_type,
                front_document=front_document,
                back_document=back_document
            )
            return redirect('main:dashboard')
        else:
            print(verification_form.errors)
    else:
        verification_form = VerificationDocumentForm()

    context = {
        'verification_form': verification_form
    }
    return render(request, 'main/id-verification.html', context)

def account_upgrade(request):
    return render(request, 'main/account-upgrade.html')


''' account setup '''
'''       profile / registration / logout            '''
# custom registration route
from django.contrib.auth.forms import UserCreationForm
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        # form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            print(username)
            user_login = authenticate(request,username=username, password=password)
            auth_login(request, user_login)
            print(auth_login(request, user_login))
            return redirect('main:profile-form')
        else:
            print(form.errors)
    else:
        # form = UserCreationForm()
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'main/register.html', context)

# create profile with the registration data 
import time
def create_profile(request):
    # POST request form logic
    if request.method == 'POST':
        # request user instance
        form = ProfileForm(request.POST,instance=request.user, files=request.FILES)
        if form.is_valid():
            # gather profile form data
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            phone_number = form.cleaned_data.get('phone_number')
            street_address = form.cleaned_data.get('street_address')
            city = form.cleaned_data.get('city')
            state = form.cleaned_data.get('state')
            postal_or_zip_code = form.cleaned_data.get('postal_or_zip_code')
            profile_picture = form.cleaned_data.get('profile_picture')
            country = form.cleaned_data.get('country')
            select_plan = form.cleaned_data.get('select_plan')
            
            '''fetch profile of currently registered and logged in user first'''
            # request user
            user = request.user
            # filter by UUID and match the user that has been created from the registration
            profile_user = Profile.objects.filter(user_id=user.user_id)

            # update the users profile with the required form data
            profile_user.update(
                first_name = first_name,
                last_name = last_name,
                phone_number = phone_number, 
                street_address=street_address,
                city = city,
                state = state, 
                postal_or_zip_code = postal_or_zip_code,
                profile_picture = profile_picture,
                country  = country,
                select_plan = select_plan 
            )

            # save the profile data to the form model 
            form.save()

            # redirect to the dashboard
            return redirect('main:dashboard')

        else:
            # print profile form errors to the console
            print(form.errors)
    else:
        # GET profile form
        form = ProfileForm()
    context = {
        'form': form
    }
    return render(request, 'main/create-profile.html', context)

# get object or 404
from django.shortcuts import get_object_or_404

def edit_profile(request):
    user = request.user
    instance = get_object_or_404(Profile, user=user)
    print(user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()     
    else:
        form = ProfileForm(instance=instance)     
    context = {
        'form': form
    }
    return render(request, 'main/edit-profile.html', context)
# logout route
@login_required(login_url='/accounts/login')
def logout_view(request):
    # logout user
    logout(request)
    return redirect('main:index')

from django.contrib.auth import get_user_model
from django.http import JsonResponse


# ajax form validation
def validate_login(request):
    email = request.GET.get('email', None)
    User = get_user_model()
    data = {
        'is_taken': User.objects.filter(email__iexact=email).exists()
    }
    return JsonResponse(data)


def validate_registration(request):
    email = request.GET.get('email', None)
    password = request.GET.get('password1', None)
    User = get_user_model()
    data = {
        'is_user': User.objects.filter(email__iexact=email).exists(),
        'password': password,
    }
    return JsonResponse(data)
