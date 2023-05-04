from django.db import models
import uuid


class Order(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    product = models.ForeignKey("UnitType", on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    # supplier = models.CharField(max_length=255)
    # requested_by = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(null=True)

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
    unit_type = models.ForeignKey("UnitType", on_delete=models.CASCADE, null=True)
    order = models.ForeignKey("Order", on_delete=models.CASCADE, null=True, blank=True)
    rfid = models.CharField(max_length=255, null=True, blank=True)
    time_warehouse = models.DateTimeField(null=True, blank=True)
    time_assy1 = models.DateTimeField(null=True, blank=True)
    time_assy2 = models.DateTimeField(null=True, blank=True)
    time_storage = models.DateTimeField(null=True, blank=True)
    sent = models.DateTimeField(null=True, blank=True)
    
class Station(models.Model):
    name = models.CharField(max_length=200)
    instruction = models.CharField(max_length=200, null=True, blank=True)


