from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import (Person, Email, Phone, Address, Website, Note,
AssociatedContact, SocialMedia, CustomField)
from .forms import (EmailForm)
# Create your views here.

def contact_list(request):
    contacts = Person.objects.order_by('last_name')
    return render(request, 'app/contact_list.html', {'contacts': contacts})

def contact_detail(request, person_uuid):
    contact = get_object_or_404(Person, id=person_uuid)
    emails = Email.objects.filter(person=person_uuid)
    phone_numbers = Phone.objects.filter(person=person_uuid)
    addresses = Address.objects.filter(person=person_uuid)
    websites = Website.objects.filter(person=person_uuid)
    notes = Note.objects.filter(person=person_uuid)
    associated_contacts = AssociatedContact.objects.filter(person=person_uuid)
    social_media = SocialMedia.objects.filter(person=person_uuid)
    custom_fields = CustomField.objects.filter(person=person_uuid)
    context = {
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
    return render(request, 'app/contact_detail.html', context)

def email_create(request, person_uuid):
    person = get_object_or_404(Person, id=person_uuid)
    if request.method == 'POST':
        form = EmailForm(request.POST)
        person_object = form.save(commit=False)
        person_object.person = person
        person_object.save()
        url = reverse('contact_detail', kwargs={'person_uuid': person_uuid})
        return HttpResponseRedirect(url)
    else:
        form = EmailForm()
        context = {'form': form, 'action': "Create"}
        return render(request, 'app/email_edit.html', context)

def email_update(request, person_uuid, email_uuid):
    person = get_object_or_404(Person, id=person_uuid)
    email = get_object_or_404(Email, id=email_uuid)
    if request.method == 'POST':
        form = EmailForm(request.POST)
        person_object = form.save(commit=False)
        person_object.person = person
        person_object.save()
        url = reverse('contact_detail', kwargs={'person_uuid': person_uuid})
        return HttpResponseRedirect(url)
    else:
        form = EmailForm(None, instance=email)
        context = {'form': form, 'action': "Create"}
        return render(request, 'app/email_edit.html', context)

def email_delete(request, person_uuid, email_uuid):
    email = get_object_or_404(Email, id=email_uuid)
    person = get_object_or_404(Person, id=person_uuid)
    context = {"email": email, "person": person}
    if request.method == "POST":
        email.delete()
        url = reverse('contact_detail', kwargs={'person_uuid': person_uuid})
        return HttpResponseRedirect(url)
    return render(request, "app/email_delete.html", context)