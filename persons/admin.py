# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import PersonForm
from django.contrib import admin
from .models import Person as PersonModel

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ['user','__str__','__str__','Person_BDate']
    form = PersonForm

admin.site.register(PersonModel)