from django.contrib import admin
from .models import *

## Class About Company


class AboutCompanyImagesInline(admin.TabularInline):
    model = About_Company_Images
    extra = 1


class AboutCompanyAdmin(admin.ModelAdmin):
    inlines = [AboutCompanyImagesInline]
    list_display = ('id', 'title', 'is_active', 'date_created')


## Class Truck


class TruckImagesImagesInline(admin.TabularInline):
    model = Truck_Images
    extra = 1


class TruckAdmin(admin.ModelAdmin):
    inlines = [TruckImagesImagesInline]
    list_display = ('id', 'title','description', 'category', 'car_weight', 'car_length', 'is_active','date_created')


## Class Blog


class BlogImagesInline(admin.TabularInline):
    model = Blog_Images
    extra = 1


class BlogAdmin(admin.ModelAdmin):
    inlines = [BlogImagesInline]
    list_display = ('id', 'title', 'category', 'description','is_active','date_created')


## Class Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','description', 'from_somewhere','to_somewhere','phone_number', 'status', 'date_created')


## Class Order


class OrderImagesInline(admin.TabularInline):
    model = Order_Images
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderImagesInline]
    list_display = ['id', 'user', 'car', 'title', 'date_created', 'from_somewhere', 'to_somewhere', 'phone_number','length_cargo', 'weight_cargo', 'mode_cargo', 'type_cargo']
    search_fields = ["title", "user", "car"]


## Class Our Services


class OurServicesImagesInline(admin.TabularInline):
    model = Our_Services_Images
    extra = 1


class OurServicesAdmin(admin.ModelAdmin):
    inlines = [OurServicesImagesInline]
    list_display = ('id', 'title','price', 'is_active')


## Class Work Principles


class WorkPrinciplesImagesInline(admin.TabularInline):
    model = Our_Services_Images
    extra = 1


class WorkPrinciplesAdmin(admin.ModelAdmin):
    inlines = [WorkPrinciplesImagesInline]
    list_display = ('id', 'title','description','about', 'date_created','is_active')


admin.site.register(WeightCargo)
admin.site.register(LengthCargo)
admin.site.register(TypeCargo)
admin.site.register(ModeCargo)
admin.site.register(Order)
admin.site.register(Category_Blog)
admin.site.register(Blog)
admin.site.register(About_Company_Images)
admin.site.register(Contact)
admin.site.register(Calculate_The_Cost)
admin.site.register(Submit_Your_Application)
admin.site.register(CategoryForTruck)
admin.site.register(User)
admin.site.register(About_Company, AboutCompanyAdmin)
admin.site.register(Truck, TruckAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Work_Principles, WorkPrinciplesAdmin)
admin.site.register(Our_Services, OurServicesAdmin)
admin.site.register(Order, OrderAdmin)



