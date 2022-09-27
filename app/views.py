from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import (Person, Email, Phone, Address, Website, Note,
AssociatedContact, SocialMedia, CustomField)
from .forms import (AddressForm, EmailForm, PhoneForm, PersonForm, SocialMediaForm, WebsiteForm)
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

def contact_create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        person_object = form.save(commit=False)
        person_object.save()
        url = reverse('contact_detail', kwargs={'person_uuid': person_object.id})
        return HttpResponseRedirect(url)
    else:
        form = PersonForm()
        context = {'form': form, 'action': "Create"}
        return render(request, 'app/contact_edit.html', context)

def contact_update(request, person_uuid):
    context = {'action': "Update"}
    person = get_object_or_404(Person, id=person_uuid)
    form = PersonForm(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        url = reverse('contact_detail', kwargs={'person_uuid': person_uuid})
        return HttpResponseRedirect(url)
    context["form"] = form
    return render(request, 'app/contact_edit.html', context)

def contact_delete(request, person_uuid):
    person = get_object_or_404(Person, id=person_uuid)
    context = {"person": person}
    if request.method == "POST":
        person.delete()
        url = reverse('contact_list')
        return HttpResponseRedirect(url)
    return render(request, "app/contact_delete.html", context)

def email_create(request, person_uuid):
    person = get_object_or_404(Person, id=person_uuid)
    if request.method == 'POST':
        form = EmailForm(request.POST)
        email_object = form.save(commit=False)
        email_object.person = person
        email_object.save()
        url = reverse('contact_detail', kwargs={'person_uuid': person_uuid})
        return HttpResponseRedirect(url)
    else:
        form = EmailForm()
        context = {'form': form, 'action': "Create"}
        return render(request, 'app/email_edit.html', context)

def email_update(request, person_uuid, email_uuid):
    context = {'action': "Update"}
    email = get_object_or_404(Email, id=email_uuid)
    form = EmailForm(request.POST or None, instance=email)
    if form.is_valid():
        form.save()
        url = reverse('contact_detail', kwargs={'person_uuid': person_uuid})
        return HttpResponseRedirect(url)
    context["form"] = form
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

def address_create(request, person_uuid):
    person = get_object_or_404(Person, id=person_uuid)
    if request.method == 'POST':
        form = AddressForm(request.POST)
        address_object = form.save(commit=False)
        address_object.person = person
        address_object.save()
        url = reverse('contact_detail', kwargs={'person_uuid': person_uuid})
        return HttpResponseRedirect(url)
    else:
        form = AddressForm()
        context = {'form': form, 'action': "Create"}
        return render(request, 'app/address_edit.html', context)

def address_update(request, person_uuid, address_uuid):
    context = {'action': "Update"}
    address = get_object_or_404(Address, id=address_uuid)
    form = AddressForm(request.POST or None, instance=address)
    if form.is_valid():
        form.save()
        url = reverse('contact_detail', kwargs={'person_uuid': person_uuid})
        return HttpResponseRedirect(url)
    context["form"] = form
    return render(request, 'app/address_edit.html', context)

def address_delete(request, person_uuid, address_uuid):
    address = get_object_or_404(Address, id=address_uuid)
    person = get_object_or_404(Person, id=person_uuid)
    context = {"address": address, "person": person}
    if request.method == "POST":
        address.delete()
        url = reverse('contact_detail', kwargs={'person_uuid': person_uuid})
        return HttpResponseRedirect(url)
    return render(request, "app/address_delete.html", context)

def website_create(request, person_uuid):
    person = get_object_or_404(Person, id=person_uuid)
    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        website_object = form.save(commit=False)
        website_object.person = person
        website_object.save()
        url = reverse('contact_detail', kwargs={'person_uuid': person_uuid})
        return HttpResponseRedirect(url)
    else:
        form = WebsiteForm()
        context = {'form': form, 'action': "Create"}
        return render(request, 'app/website_edit.html', context)

def website_update(request, person_uuid, website_uuid):
    context = {'action': "Update"}
    website = get_object_or_404(Website, id=website_uuid)
    form = WebsiteForm(request.POST or None, instance=website)
    if form.is_valid():
        form.save()
        url = reverse('contact_detail', kwargs={'person_uuid': person_uuid})
        return HttpResponseRedirect(url)
    context["form"] = form
    return render(request, 'app/website_edit.html', context)

def website_delete(request, person_uuid, website_uuid):
    website = get_object_or_404(Website, id=website_uuid)
    person = get_object_or_404(Person, id=person_uuid)
    context = {"website": website, "person": person}
    if request.method == "POST":
        website.delete()
        url = reverse('contact_detail', kwargs={'person_uuid': person_uuid})
        return HttpResponseRedirect(url)
    return render(request, "app/website_delete.html", context)

def phone_number_create(request, person_uuid):
    person = get_object_or_404(Person, id=person_uuid)
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        phone_object = form.save(commit=False)
        phone_object.person = person
        phone_object.save()
        url = reverse('contact_detail', kwargs={'person_uuid': person_uuid})
        return HttpResponseRedirect(url)
    else:
        form = PhoneForm()
        context = {'form': form, 'action': "Create"}
        return render(request, 'app/phone_edit.html', context)

def phone_number_update(request, person_uuid, phone_number_uuid):
    context = {'action': "Update"}
    phone = get_object_or_404(Phone, id=phone_number_uuid)
    form = PhoneForm(request.POST or None, instance=phone)
    if form.is_valid():
        form.save()
        url = reverse('contact_detail', kwargs={'person_uuid': person_uuid})
        return HttpResponseRedirect(url)
    context["form"] = form
    return render(request, 'app/phone_edit.html', context)

def phone_number_delete(request, person_uuid, phone_number_uuid):
    phone = get_object_or_404(Phone, id=phone_number_uuid)
    person = get_object_or_404(Person, id=person_uuid)
    context = {"phone": phone, "person": person}
    if request.method == "POST":
        phone.delete()
        url = reverse('contact_detail', kwargs={'person_uuid': person_uuid})
        return HttpResponseRedirect(url)
    return render(request, "app/phone_delete.html", context)

def social_media_create(request, person_uuid):
    person = get_object_or_404(Person, id=person_uuid)
    if request.method == 'POST':
        form = SocialMediaForm(request.POST)
        social_media_object = form.save(commit=False)
        social_media_object.person = person
        social_media_object.save()
        url = reverse('contact_detail', kwargs={'person_uuid': person_uuid})
        return HttpResponseRedirect(url)
    else:
        form = SocialMediaForm()
        context = {'form': form, 'action': "Create"}
        return render(request, 'app/social_media_edit.html', context)

def social_media_update(request, person_uuid, social_media_uuid):
    context = {'action': "Update"}
    social_media = get_object_or_404(SocialMedia, id=social_media_uuid)
    form = SocialMediaForm(request.POST or None, instance=social_media)
    if form.is_valid():
        form.save()
        url = reverse('contact_detail', kwargs={'person_uuid': person_uuid})
        return HttpResponseRedirect(url)
    context["form"] = form
    return render(request, 'app/social_media_edit.html', context)

def social_media_delete(request, person_uuid, social_media_uuid):
    social_media = get_object_or_404(SocialMedia, id=social_media_uuid)
    person = get_object_or_404(Person, id=person_uuid)
    context = {"social_media": social_media, "person": person}
    if request.method == "POST":
        social_media.delete()
        url = reverse('contact_detail', kwargs={'person_uuid': person_uuid})
        return HttpResponseRedirect(url)
    return render(request, "app/social_media_delete.html", context)
