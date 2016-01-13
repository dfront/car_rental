from django.contrib import admin
from client.models import Client, ClientCnhCategory, CnhCategory

class ClientCnhCategoryInline(admin.TabularInline):
    model = ClientCnhCategory

class ClientAdmin(admin.ModelAdmin):
    list_display = ("user","name","cpf","cnhNumber")
    inlines = [ClientCnhCategoryInline,]

class CnhCategoryAdmin(admin.ModelAdmin):
    list_display = ("category","description")

class ClientCnhCategoryAdmin(admin.ModelAdmin):
    list_display = ('client','category')


admin.site.register(Client,ClientAdmin)
admin.site.register(CnhCategory,CnhCategoryAdmin)
admin.site.register(ClientCnhCategory,ClientCnhCategoryAdmin)
