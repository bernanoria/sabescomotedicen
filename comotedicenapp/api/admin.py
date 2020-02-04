# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import ( Categoria, Dicho
)

admin.site.register(Categoria)
admin.site.register(Dicho)
# Register your models here.
