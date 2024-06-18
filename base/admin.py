from django.contrib import admin as a

from .models import *

a.site.register(Customer)
a.site.register(Visit)
a.site.register(ButtonClick)