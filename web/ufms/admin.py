from django.contrib import admin
from ufms.models import Ufms


# Register your models here.

class UfmsModelAdmin(admin.ModelAdmin):
    search_fields = ['name', 'number']


admin.site.register(Ufms, UfmsModelAdmin)
