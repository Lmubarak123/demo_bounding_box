from django.contrib import admin
from demo_app2.models import Contact
# Register your models here.

admin.site.register(Contact)

'''
from django.contrib import admin

from demo_app.models import Entities,Contact

class contactAdmin(admin.ModelAdmin):
    fields = ['Name', 'email','phone','desc']

admin.site.register(Contact, contactAdmin)

'''