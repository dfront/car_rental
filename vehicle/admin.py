from django.contrib import admin
from vehicle.models import Vehicle, VehicleCategory, VehicleModel
from client.models import CnhCategory

class VehicleAdmin(admin.ModelAdmin):
    list_display = ("board","category","model","km")

class VehicleCategoryAdmin(admin.ModelAdmin):
    list_display = ("category","chnCategoryPermitedStr")

    def chnCategoryPermitedStr(self,obj):
        return obj.cnhCategoryPermited

class VehicleModelAdmin(admin.ModelAdmin):
    list_display = ("model","category")

admin.site.register(Vehicle,VehicleAdmin)
admin.site.register(VehicleModel,VehicleModelAdmin)
admin.site.register(VehicleCategory,VehicleCategoryAdmin)
