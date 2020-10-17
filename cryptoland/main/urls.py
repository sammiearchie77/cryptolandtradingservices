from django.urls import path

'''
home, privacy policy, Payment Policy views
'''

from .views import index, logout_view,contact, about, register,terms_and_condition, privacy_policy, safety_of_funds

# dashboard routes
from .views import dashboard, id_verification, account_upgrade, create_profile,edit_profile, fund_account, trading_history, withdraw_funds

# validation routes
from .views import validate_login, validate_registration

app_name = 'main'

urlpatterns = [
    # home page
    path('', index, name="index"),
    # about
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    # terms and conditions, Privacy policy
    path('terms-and-conditions/', terms_and_condition, name='terms-and-conditions'),
    path('privacy-policy', privacy_policy, name='privacy-policy'),
    path('safety-of-funds', safety_of_funds, name='safety-of-funds'),
    # dashboard routes
    path('dashboard/', dashboard, name="dashboard"),
    path('fund-account/', fund_account, name='fund-account'), 
    path('trading-history/', trading_history, name='trading-history'),
    path('withdraw-funds/', withdraw_funds, name='withdraw-funds'),
    path('id-verification/', id_verification, name='id-verification'), 
    path('logout/', logout_view, name='logout'),
    path('account/upgrade', account_upgrade, name='account-upgrade'),
    # registration and login routes
    path('register/', register, name='register'),
    path('profile/create', create_profile, name='profile-form' ), 
    path('profile/edit', edit_profile, name='edit-profile' ),

    # validation routes
    path('validate/login', validate_login, name='validate-login'),
    path('validate/register', validate_registration, name='validate-registration')
    
]
