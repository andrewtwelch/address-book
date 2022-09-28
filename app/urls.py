"""addressbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (address_create, address_delete, address_update, associated_contact_create, associated_contact_delete,
associated_contact_update, contact_create, contact_update, contact_delete, contact_list, contact_detail, email_create,
email_update, email_delete, phone_number_create, phone_number_update, phone_number_delete, social_media_create,
social_media_delete, social_media_update, website_create, website_update, website_delete, custom_field_create,
custom_field_update, custom_field_delete, note_create, note_update, note_delete)

urlpatterns = [
    path('', contact_list, name="contact_list"),
    path('contact/<uuid:person_uuid>/', contact_detail, name="contact_detail"),
    path('contact/create/', contact_create, name="contact_create"),
    path('contact/update/<uuid:person_uuid>/', contact_update, name="contact_update"),
    path('contact/delete/<uuid:person_uuid>/', contact_delete, name="contact_delete"),
    path('contact/<uuid:person_uuid>/email/create/', email_create, name="email_create"),
    path('contact/<uuid:person_uuid>/email/update/<uuid:email_uuid>', email_update, name="email_update"),
    path('contact/<uuid:person_uuid>/email/delete/<uuid:email_uuid>', email_delete, name="email_delete"),
    path('contact/<uuid:person_uuid>/address/create/', address_create, name="address_create"),
    path('contact/<uuid:person_uuid>/address/update/<uuid:address_uuid>', address_update, name="address_update"),
    path('contact/<uuid:person_uuid>/address/delete/<uuid:address_uuid>', address_delete, name="address_delete"),
    path('contact/<uuid:person_uuid>/website/create/', website_create, name="website_create"),
    path('contact/<uuid:person_uuid>/website/update/<uuid:website_uuid>', website_update, name="website_update"),
    path('contact/<uuid:person_uuid>/website/delete/<uuid:website_uuid>', website_delete, name="website_delete"),
    path('contact/<uuid:person_uuid>/phone_number/create/', phone_number_create, name="phone_number_create"),
    path('contact/<uuid:person_uuid>/phone_number/update/<uuid:phone_number_uuid>', phone_number_update, name="phone_number_update"),
    path('contact/<uuid:person_uuid>/phone_number/delete/<uuid:phone_number_uuid>', phone_number_delete, name="phone_number_delete"),
    path('contact/<uuid:person_uuid>/social_media/create/', social_media_create, name="social_media_create"),
    path('contact/<uuid:person_uuid>/social_media/update/<uuid:social_media_uuid>', social_media_update, name="social_media_update"),
    path('contact/<uuid:person_uuid>/social_media/delete/<uuid:social_media_uuid>', social_media_delete, name="social_media_delete"),
    path('contact/<uuid:person_uuid>/associated_contact/create/', associated_contact_create, name="associated_contact_create"),
    path('contact/<uuid:person_uuid>/associated_contact/update/<uuid:associated_contact_uuid>', associated_contact_update, name="associated_contact_update"),
    path('contact/<uuid:person_uuid>/associated_contact/delete/<uuid:associated_contact_uuid>', associated_contact_delete, name="associated_contact_delete"),
    path('contact/<uuid:person_uuid>/custom_field/create/', custom_field_create, name="custom_field_create"),
    path('contact/<uuid:person_uuid>/custom_field/update/<uuid:custom_field_uuid>', custom_field_update, name="custom_field_update"),
    path('contact/<uuid:person_uuid>/custom_field/delete/<uuid:custom_field_uuid>', custom_field_delete, name="custom_field_delete"),
    path('contact/<uuid:person_uuid>/note/create/', note_create, name="note_create"),
    path('contact/<uuid:person_uuid>/note/update/<uuid:note_uuid>', note_update, name="note_update"),
    path('contact/<uuid:person_uuid>/note/delete/<uuid:note_uuid>', note_delete, name="note_delete"),
]
