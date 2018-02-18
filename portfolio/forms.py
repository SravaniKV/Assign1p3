
from django import forms
from .models import Customer, Investment, Stock, MutualFunds
from django.contrib.auth.models import User
import re    # It is regular expressions library
from django.contrib.auth.forms import UserCreationForm



class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cust_number', 'name', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone',)


class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = (
            'customer', 'category', 'description', 'acquired_value', 'acquired_date', 'recent_value',
            'recent_date',)


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ('customer', 'symbol', 'name', 'shares', 'purchase_price', 'purchase_date',)

class MutualFundsForm(forms.ModelForm):
    class Meta:
        model = MutualFunds
        fields = ('customer','category','description','units','acquired_value','acquired_date','recent_value','recent_date', )



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    password1 = forms.CharField(label=("Password"),widget=forms.PasswordInput, help_text= ("Your password can not be too similar to your other personal information.Your password must contain at least 8 characters."
                                                                                           "Your password can't be a commonly used password.Your password can't be entirely numeric."))
    password2 = forms.CharField(label=("Password confirmation"),widget=forms.PasswordInput,
                                help_text=("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )