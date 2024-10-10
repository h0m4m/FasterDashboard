from django.contrib import admin
from django.utils.html import format_html
from .models import User, Contract, Fine, Car, Driver

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'display_profile_picture')
    search_fields = ['id', 'first_name', 'last_name']
    
    def display_profile_picture(self, obj):
        if obj.profile_picture:
            return format_html('<img src="{}" width="150"/>', obj.profile_picture.url)
        return 'No Image'
    display_profile_picture.short_description = 'Profile Picture'



@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('license_plate_number', 'kilometer', 'car_name', 'car_year', 'car_color', 'display_car_picture')
    search_fields = ['license_plate_number', 'car_name', 'car_year', 'car_color']

    def display_car_picture(self, obj):
        if obj.car_picture:
            image_url = obj.car_picture.url
            return format_html('<a href="{}" target="_blank"><img src="{}" width="50" style="max-width:200px;"/></a>', image_url, image_url)
        return 'No Image'

    display_car_picture.short_description = 'Car Picture'



@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'display_contract_image', 'pickup_date', 'return_date', 'is_active', 'deposit_status', 'display_exterior_images', 'display_interior_images', 'display_invoice_image' )
    search_fields = ['user__first_name', 'user__last_name', 'car__car_name', 'car__car_year', 'car__car_color', 'pickup_date', 'return_date']


    def display_contract_image(self, obj):
        if obj.contract_image:
            image_url = obj.contract_image.url
            return format_html('<a href="{}" target="_blank"><img src="{}" width="50" style="max-width:200px;"/></a>', image_url, image_url)
        return 'No Image'
    display_contract_image.short_description = 'Contract Image'
    
    def display_exterior_images(self, obj):
        images_html = ''
        for field in ['car_exterior_image1', 'car_exterior_image2', 'car_exterior_image3', 'car_exterior_image4', 'car_exterior_image5']:
            image = getattr(obj, field)
            if image:
                images_html += f'<a href="{image.url}" target="_blank"><img src="{image.url}" width="50" style="max-width:200px;"/></a>'
        return format_html(images_html)
    display_exterior_images.short_description = 'Report Exterior Images'

    def display_interior_images(self, obj):
        images_html = ''
        for field in ['car_interior_image1', 'car_interior_image2', 'car_interior_image3', 'car_interior_image4', 'car_interior_image5']:
            image = getattr(obj, field)
            if image:
                images_html += f'<a href="{image.url}" target="_blank"><img src="{image.url}" width="50" style="max-width:200px;"/></a>'
        return format_html(images_html)
    display_interior_images.short_description = 'Report Interior Images'

    def display_invoice_image(self, obj):
        if obj.invoice_image:
            image_url = obj.invoice_image.url
            return format_html('<a href="{}" target="_blank"><img src="{}" width="50" style="max-width:200px;"/></a>', image_url, image_url)
        return 'No Image'
    display_invoice_image.short_description = 'Invoice Image'


@admin.register(Fine)
class FineAdmin(admin.ModelAdmin):
    list_display = ('contract', 'display_fine_picture', 'fine_number', 'fine_type', 'fine_date', 'amount',)
    search_fields = ['contract__user__first_name', 'contract__user__last_name', 'contract__car__car_name', 'fine_type', 'fine_number', 'fine_date', 'amount']  # Enable search on related fields

    def display_fine_picture(self, obj):
        if obj.fine_picture:
            image_url = obj.fine_picture.url
            return format_html('<a href="{}" target="_blank"><img src="{}" width="50" style="max-width:200px;"/></a>', image_url, image_url)
        return 'No Image'
    display_fine_picture.short_description = 'Fine Image'

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'display_profile_picture')
    search_fields = ['id', 'first_name', 'last_name']
    
    def display_profile_picture(self, obj):
        if obj.profile_picture:
            return format_html('<img src="{}" width="150"/>', obj.profile_picture.url)
        return 'No Image'
    display_profile_picture.short_description = 'Profile Picture'


