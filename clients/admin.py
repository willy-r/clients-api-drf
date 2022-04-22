from django.contrib import admin

from clients.models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email','cpf', 'rg', 'cellphone', 'is_active')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'cpf')
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    list_per_page = 25
    ordering = ('name',)

admin.site.register(Client, ClientAdmin)
