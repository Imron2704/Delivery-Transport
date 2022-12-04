from django.contrib import admin
from .models import *


class AboutCompanyImagesInline(admin.TabularInline):
    model = About_Company_Images
    extra = 1


class AboutCompanyAdmin(admin.ModelAdmin):
    inlines = [AboutCompanyImagesInline]
    list_display = ('id', 'title', 'is_active', 'date_created')
    # readonly_fields = ('date_created')

admin.site.register(About_Company, AboutCompanyAdmin)

admin.register(CategoryForTruck)
admin.register(WeightCargo)
admin.register(LengthCargo)
admin.register(TypeCargo)
admin.register(ModeCargo)
admin.register(Order)
admin.register(Truck)
admin.register(Blog_About_Truck)
admin.register(Blog)
admin.register(About_Company)
admin.register(About_Company_Images)
admin.register(Contact)
admin.register(About_Company)
admin.register(Calculate_The_Cost)
admin.register(Submit_Your_Application)
admin.register(User)


