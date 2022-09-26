import uuid
from django.db import models
from django_countries.fields import CountryField

# Create your models here.

class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    company = models.CharField(max_length=50, blank=True)
    birthday = models.DateField(blank=True, null=True)

class Email(models.Model):
    EMAIL_TYPE_CHOICES = [
        ('PERSONAL', 'Personal'),
        ('WORK', 'Work'),
        ('SCHOOL', 'School'),
        ('OTHER', 'Other')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=EMAIL_TYPE_CHOICES)
    email = models.EmailField()

class Phone(models.Model):
    PHONE_TYPE_CHOICES = [
        ('MOBILE', 'Mobile'),
        ('HOME', 'Home'),
        ('WORK', 'Work'),
        ('SCHOOL', 'School'),
        ('OTHER', 'Other')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=PHONE_TYPE_CHOICES)
    number = models.CharField(max_length=30)

class Address(models.Model):
    ADDRESS_TYPE_CHOICES = [
        ('HOME', 'Home'),
        ('WORK', 'Work'),
        ('SCHOOL', 'School'),
        ('OTHER', 'Other')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=ADDRESS_TYPE_CHOICES)
    street1 = models.CharField(max_length=150)
    street2 = models.CharField(max_length=150)
    suburb = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postcode = models.CharField(max_length=10)
    country = CountryField()

class Website(models.Model):
    WEBSITE_TYPE_CHOICES = [
        ('PERSONAL', 'Personal'),
        ('WORK', 'Work'),
        ('OTHER', 'Other')
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=10, choices=WEBSITE_TYPE_CHOICES)
    url = models.URLField()


class Note(models.model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    note = models.TextField()

class AssociatedContact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    associated_contact = models.ForeignKey('Person', on_delete=models.CASCADE)
    relation = models.CharField(max_length=50)

class SocialMedia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    website_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, blank=True)
    url = models.URLField(blank=True)

class CustomField(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    field_name = models.CharField(max_length=50)
    field_contents = models.CharField(max_length=200)
