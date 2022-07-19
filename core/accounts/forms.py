from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm,
                                       SetPasswordForm)

from accounts.models import Account, Profile
from accounts.models import Account as UserBase


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=50, help_text="Required. Add a valid email address.")
    first_name = forms.CharField(label='First Name', min_length=2, max_length=30, widget=forms.TextInput(attrs={'autofocus': True}))
    last_name = forms.CharField(label='Last Name', min_length=2, max_length=30,)

    class Meta:
        model = Account
        fields = ('email', 'first_name', "last_name", 'password1', 'password2',)

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % email)

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     try:
    #         account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
    #     except Account.DoesNotExist:
    #         return username
    #     raise forms.ValidationError('Username "%s" is already in use.' % username)


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid Login Details")

class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'hide_email') #  'username',

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

    def save(self, commit=True):
        account = super(AccountUpdateForm, self).save(commit=False)
        account.email = self.cleaned_data['email'].lower()
        account.first_name = self.cleaned_data['first_name']
        account.last_name = self.cleaned_data['last_name']
        account.hide_email = self.cleaned_data['hide_email']
        if commit:
            account.save()
        return account

# class ProfileImageUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Account
#         fields = ('profile_image',)

#     def save(self, commit=True):
#         account = super(ProfileImageUpdateForm, self).save(commit=False)
#         account.profile_image = self.cleaned_data['profile_image']
#         if commit:
#             account.save()
#         return account


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','phone_number',)
        

class PwdResetForm(PasswordResetForm):

    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'form-email'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        u = UserBase.objects.filter(email=email)
        if not u:
            raise forms.ValidationError(
                'Unfortunatley we can not find that email address')
        return email


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-newpass'}))
    new_password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-new-pass2'}))