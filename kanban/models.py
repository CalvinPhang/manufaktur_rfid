from django.db import models
import uuid


class Order(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    product = models.ForeignKey("UnitType", on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    # supplier = models.CharField(max_length=255)
    # requested_by = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)
    # delivery_date = models.DateField()

class UnitType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    
    
class PartType(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Inventory(models.Model):
    unit_type = models.ForeignKey("UnitType", on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    
class PartsInventory(models.Model):
    part_type = models.ForeignKey("PartType", on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()

class UnitPartsBom(models.Model):
    unit_type = models.ForeignKey("UnitType", on_delete=models.CASCADE, null=True)
    part_type = models.ForeignKey("PartType", on_delete=models.CASCADE, null=True)
    part_quantity = models.IntegerField()
    
    
class Products(models.Model):
    product_code = models.CharField(max_length=200)
    order = models.ForeignKey("Order", on_delete=models.CASCADE, null=True)
    rfid = models.CharField(max_length=255)
    
    


