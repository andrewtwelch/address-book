from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Person)
admin.site.register(Email)
admin.site.register(Phone)
admin.site.register(Address)
admin.site.register(Website)
admin.site.register(Note)
admin.site.register(AssociatedContact)
admin.site.register(SocialMedia)
admin.site.register(CustomField)