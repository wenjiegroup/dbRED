from django.contrib import admin

# Register your models here.
from .models import Human_Rnaedit


class Human_RnaeditAdmin(admin.ModelAdmin):
    list_display=('name', 'Chr', 'position')
    list_filter=('add_time', 'Chr', 'method','Cellline')
    search_fields=('name', 'Chr', 'position')

admin.site.register(Human_Rnaedit, Human_RnaeditAdmin)
