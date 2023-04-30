from django.contrib import admin
from . import models

@admin.register(models.UnitType)
class UnitAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name", 
    )

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "unit_name",
        "quantity",
        "order_date",
    )
    
    @admin.display(ordering='product__name', description='Product ID')
    def unit_name(self, obj):
        return obj.product.name
    

@admin.register(models.PartType)
class PartAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name", 
    )
    
@admin.register(models.PartsInventory)
class PartInvAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "part_name",
        "quantity"
    )
    
    @admin.display(ordering='part_type__name', description='Part Type')
    def part_name(self, obj):
        return obj.part_type.name

@admin.register(models.UnitPartsBom)
class BOMAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "unit_name",
        "part_name",
        "part_quantity"
    )
    
    @admin.display(ordering='part_type__name', description='Part Type')
    def part_name(self, obj):
        return obj.part_type.name
    
    @admin.display(ordering='unit_type__name', description='Unit Type')
    def unit_name(self, obj):
        return obj.unit_type.name
    
@admin.register(models.Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product_code",
        "order",
        "rfid"
    )