from django.contrib import admin

from data.models import d4826085213, d6162070130, d6168077734, StatisticFind


class d4826085213ModelAdmin(admin.ModelAdmin):
    search_fields = ['pk', 'guid', 'fio']
    list_display = ('get_instance',)

    @staticmethod
    def get_instance(instance):
        return instance


class d6162070130ModelAdmin(admin.ModelAdmin):
    search_fields = ['pk', 'guid', 'fio']
    list_display = ('get_instance',)

    @staticmethod
    def get_instance(instance):
        return instance


class d6168077734ModelAdmin(admin.ModelAdmin):
    search_fields = ['pk', 'guid', 'fio']
    list_display = ('get_instance',)

    @staticmethod
    def get_instance(instance):
        return instance


class StatisticFindModelAdmin(admin.ModelAdmin):
    search_fields = ['model_name', 'id_find']
    list_display = ('get_instance',)

    @staticmethod
    def get_instance(instance):
        return instance


admin.site.register(d4826085213, d4826085213ModelAdmin)
admin.site.register(d6162070130, d6162070130ModelAdmin)
admin.site.register(d6168077734, d6168077734ModelAdmin)
admin.site.register(StatisticFind, StatisticFindModelAdmin)
