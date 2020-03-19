from django.contrib import admin
from .models import Search


class SearchAdmin(admin.ModelAdmin):
    list_display = ['search', 'created']


admin.site.register(Search, SearchAdmin)


# Register your models here.
