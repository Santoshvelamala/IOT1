# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Traffic

admin.site.register(Traffic)

from .models import OverSpeed

admin.site.register(OverSpeed)
