from django import forms
from .models import (Address, AssociatedContact, Person, Phone, Email, SocialMedia, Website)

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

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        exclude = ('id',)

class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = '__all__'
        exclude = ('id', 'person')

class SocialMediaForm(forms.ModelForm):
    class Meta:
        model = SocialMedia
        fields = '__all__'
        exclude = ('id', 'person')

class AssociatedContactForm(forms.ModelForm):
    class Meta:
        model = AssociatedContact
        fields = '__all__'
        exclude = ('id', 'person')