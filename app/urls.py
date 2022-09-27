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
from .views import (address_create, address_delete, address_update, contact_list, contact_detail, email_create, email_update, email_delete, website_create, website_update, website_delete)

urlpatterns = [
    path('', contact_list, name="contact_list"),
    path('contact/<uuid:person_uuid>/', contact_detail, name="contact_detail"),
    path('contact/<uuid:person_uuid>/email/create/', email_create, name="email_create"),
    path('contact/<uuid:person_uuid>/email/update/<uuid:email_uuid>', email_update, name="email_update"),
    path('contact/<uuid:person_uuid>/email/delete/<uuid:email_uuid>', email_delete, name="email_delete"),
    path('contact/<uuid:person_uuid>/address/create/', address_create, name="address_create"),
    path('contact/<uuid:person_uuid>/address/update/<uuid:address_uuid>', address_update, name="address_update"),
    path('contact/<uuid:person_uuid>/address/delete/<uuid:address_uuid>', address_delete, name="address_delete"),
    path('contact/<uuid:person_uuid>/website/create/', website_create, name="website_create"),
    path('contact/<uuid:person_uuid>/website/update/<uuid:website_uuid>', website_update, name="website_update"),
    path('contact/<uuid:person_uuid>/website/delete/<uuid:website_uuid>', website_delete, name="website_delete"),
]
