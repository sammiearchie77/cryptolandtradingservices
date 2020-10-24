from django.urls import path

'''
home, privacy policy, Payment Policy views
'''

from .views import index,faq, logout_view,contact, about, register,terms_and_condition, privacy_policy, safety_of_funds

# dashboard routes
from .views import dashboard, id_verification, account_upgrade, create_profile,edit_profile, fund_account, transactions, withdraw_funds

# validation routes
from .views import validate_login, validate_registration

from . import views

# settings 
from django.conf import settings 
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    # home page
    path('', index, name="index"),
    # about
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('services/', views.services, name='services'),
    # terms and conditions, Privacy policy
    path('terms-of-services/', terms_and_condition, name='terms-of-services'),
    path('privacy-policy', privacy_policy, name='privacy-policy'),
    path('safety-of-funds', safety_of_funds, name='safety-of-funds'),
    path('pricing/', views.pricing, name='pricing'),
    # frequently asked questions 
    
    path('faq/', faq ,name='faq'),
    # dashboard routes
    path('dashboard/', dashboard, name="dashboard"),
    path('fund-account/', fund_account, name='fund-account'), 
    path('transactions/', transactions, name='transactions'),
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
urlpatterns += static(
        settings.STATIC_URL, 
        document_root=settings.STATIC_ROOT
    )

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(
#         settings.MEDIA_URL, 
#         document_root=settings.MEDIA_ROOT
#     )