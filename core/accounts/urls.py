from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .import views

from .views import (register_view, logout_view, login_view, account_activate,account_view, edit_account_view, edit_user_profile_view)

from .forms import (PwdResetConfirmForm, PwdResetForm)

app_name = "account"

urlpatterns = [
     # Beginning Reset password
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="account/user/password_reset_form.html",
                                                                 success_url='password_reset_email_confirm',
                                                                 email_template_name='account/user/password_reset_email.html',
                                                                 form_class=PwdResetForm), name='pwdreset'),
                                                                 
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='account/user/password_reset_confirm.html',
                                                                                               success_url='password_reset_complete',
                                                                                               form_class=PwdResetConfirmForm),
                                                                                               name="password_reset_confirm"),

    path('password_reset/password_reset_email_confirm/',
         TemplateView.as_view(template_name="account/user/reset_status.html"), name='password_reset_done'),

    path('password_reset_confirm/Mg/password_reset_complete/',
         TemplateView.as_view(template_name="account/user/reset_status.html"), 
         name='password_reset_complete'),

    # End of Reset Password

    #Account activation
    path("activate/<slug:uidb64>/<slug:token>)/", account_activate, name="activate"),

     #Authentication
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('sign-up/',views.sign_up, name='sign-up'),
    path('logout/', logout_view, name='logout'),
    path('contact/',views.contact, name='contact'),
    path('product_grid/', views.product_grid, name='product_grid'),
    path('login/',views.login, name="login"),
    path('product_detail/',views.product_detail, name="product_detail"),
    path('profile/', views.profile, name='profile'),
    path('thanks/',views.thanks, name='thanks'),
    path('checkout/',views.checkout, name='checkout'),
    path('forms',views.forms, name='forms' ), 

    # Accounts
    path('<user_id>/', account_view, name='user-account-view'),
    path('<user_id>/edit/', edit_account_view, name='edit-account'),

    # Profile
    path('<user_id>/profile/update/', edit_user_profile_view, name='edit-user-profile-view'),

    #INDEX FILE  
    path('',views.index, name='index'),

]
