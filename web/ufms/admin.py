from django.contrib import admin
from ufms.models import Ufms


# Register your models here.

class UfmsModelAdmin(admin.ModelAdmin):
    search_fields = ['name', 'number']
    list_display = ('get_instance',)

    @staticmethod
    def get_instance(instance):
        return instance


admin.site.register(Ufms, UfmsModelAdmin)
