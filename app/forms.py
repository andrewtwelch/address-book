from django import forms
from .models import (Address, Email)

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = '__all__'
        widgets = {'person': forms.HiddenInput()}
        #exclude = ('id', 'person',)

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
        exclude = ('id', 'person',)