import uuid
from django.db import models
from django_countries.fields import CountryField

# Create your models here.

class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=50, blank=True)
    birthday = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Email(models.Model):
    EMAIL_TYPE_CHOICES = [
        ('Personal', 'Personal'),
        ('Work', 'Work'),
        ('School', 'School'),
        ('Other', 'Other')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=EMAIL_TYPE_CHOICES)
    email = models.EmailField()

    def __str__(self):
        return str(self.person) + " - " + self.type + " - " + self.email

class Phone(models.Model):
    PHONE_TYPE_CHOICES = [
        ('Mobile', 'Mobile'),
        ('Home', 'Home'),
        ('Work', 'Work'),
        ('School', 'School'),
        ('Other', 'Other')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=PHONE_TYPE_CHOICES)
    number = models.CharField(max_length=30)

    def __str__(self):
        return str(self.person) + " - " + self.type + " - " + self.number

class Address(models.Model):
    ADDRESS_TYPE_CHOICES = [
        ('Home', 'Home'),
        ('Work', 'Work'),
        ('School', 'School'),
        ('Other', 'Other')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=ADDRESS_TYPE_CHOICES)
    street1 = models.CharField(max_length=150)
    street2 = models.CharField(max_length=150, blank=True)
    suburb = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postcode = models.CharField(max_length=10)
    country = CountryField()

    def __str__(self):
        return str(self.person) + " - " + self.type + " - " + self.street1
    
    @property
    def get_readable_str(self):
        text = self.street1
        if (self.street2):
            text += " " + self.street2
        text += ", " + self.suburb + " " + self.state + " " + self.postcode + ", " + self.country.name
        return text

class Website(models.Model):
    WEBSITE_TYPE_CHOICES = [
        ('Personal', 'Personal'),
        ('Work', 'Work'),
        ('Other', 'Other')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=WEBSITE_TYPE_CHOICES)
    url = models.URLField()

    def __str__(self):
        return str(self.person) + " - " + self.type + " - " + self.url


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    note = models.TextField()

    def __str__(self):
        return str(self.person) + " - Note - " + str(self.id)

class AssociatedContact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    associated_contact = models.ForeignKey('Person', on_delete=models.CASCADE,related_name="associated_contact")
    relation = models.CharField(max_length=50)

    def __str__(self):
        return str(self.person) + " - " + self.relation + " - " + str(self.associated_contact)

class SocialMedia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    website_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return str(self.person) + " - " + self.website_name + " - " + self.username

class CustomField(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    field_name = models.CharField(max_length=50)
    field_contents = models.CharField(max_length=200)

    def __str__(self):
        return str(self.person) + " - " + self.field_name
