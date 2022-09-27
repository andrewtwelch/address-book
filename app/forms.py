from django import forms
from .models import (Address, Email, Website)

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = '__all__'
        exclude = ('id', 'person',)

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
        exclude = ('id', 'person',)

class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = '__all__'
        exclude = ('id', 'person',)