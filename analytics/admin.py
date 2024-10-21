from django.contrib import admin as a

from .models import Visit

class VisitAdmin(a.ModelAdmin):

    list_display = ['city', 'mobile', 'entered_at', 'left_at']

a.site.register(Visit, VisitAdmin)