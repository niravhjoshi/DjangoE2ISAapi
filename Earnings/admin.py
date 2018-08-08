# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import EarningsEntry as EarningModel
# Register your models here.
admin.site.register(EarningModel)

