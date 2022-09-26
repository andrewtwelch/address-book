from django.shortcuts import render, get_object_or_404
from .models import (Person, Email, Phone, Address, Website, Note,
AssociatedContact, SocialMedia, CustomField)
# Create your views here.

def contact_list(request):
    contacts = Person.objects.all()
    return render(request, 'app/contact_list.html', {'contacts': contacts})

def contact_detail(request, uuid):
    contact = get_object_or_404(Person, id=uuid)
    emails = Email.objects.filter(person=uuid)
    phone_numbers = Phone.objects.filter(person=uuid)
    addresses = Address.objects.filter(person=uuid)
    websites = Website.objects.filter(person=uuid)
    notes = Note.objects.filter(person=uuid)
    associated_contacts = AssociatedContact.objects.filter(person=uuid)
    social_media = SocialMedia.objects.filter(person=uuid)
    custom_fields = CustomField.objects.filter(person=uuid)
    detail_dict = {
        'contact': contact,
        'emails': emails,
        'phone_numbers': phone_numbers,
        'addresses': addresses,
        'websites': websites,
        'notes': notes,
        'associated_contacts': associated_contacts,
        'social_media': social_media,
        'custom_fields': custom_fields,
    }
    return render(request, 'app/contact_detail.html', detail_dict)
