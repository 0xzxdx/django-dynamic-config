from django.contrib import admin
from .models import DynamicConfig

# Register your models here.


@admin.register(DynamicConfig)
class DynamicConfigAdmin(admin.ModelAdmin):
    list_display = ("id", 'key', 'value', 'value_type', "is_show", "desc")
    list_filter = ('value_type', "is_show")
    search_fields = ('key',)
