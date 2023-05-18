from django.shortcuts import render
import datetime
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Order, UnitType, PartsInventory, UnitPartsBom, Products, Station, UnitStorage, PartType

def order_input(request):
    return render(request, 'barcode_order.html')

class OrderPost(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        content = request.data.copy()["content"]
        arr = content.split(',')
        dictt = {}
        for i in arr:
            key, value = i.split(':')
            dictt[key] = value
        print(dictt)
        unit = UnitType.objects.get(name=dictt['product'])
        # Checking inventory
        parts = UnitPartsBom.objects.filter(unit_type=unit)
        for part in parts:
            parts_inventory = PartsInventory.objects.get(part_type=part.part_type)
            if parts_inventory.quantity - part.part_quantity < 0:
                return Response({'msg': "Parts not sufficient"})
            
        # Create Order  
        order = Order(
            id = dictt["ID"],
            product = unit,
            quantity = int(dictt["qt"]),
            order_date = datetime.datetime.now()
        )
        order.save()
        
        # Create Product
        latest_product = Products.objects.filter(unit_type=unit).last()
        latest_product_code = latest_product.product_code
        unit_type = latest_product_code[0]
        increment = int(latest_product_code[1:])
        increment += 1
        product_code = unit_type + '0'*(4-(len(str(increment)))) + str(increment)
        product = Products(
            product_code = product_code,
            unit_type = unit,
        )
        product.save()
        return Response({'msg': 'order received'})

class BomProduct(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        product_code = request.data['product_code']
        product = Products.objects.get(product_code=product_code)
        product.time_warehouse = datetime.datetime.now()
        product.save()
        station = Station.objects.get(name='Warehouse')
        station.instruction = product.unit_type.name
        station.save()
        parts = UnitPartsBom.objects.filter(unit_type=product.unit_type)
        data = {}
        for part in parts:
            parts_inventory = PartsInventory.objects.get(part_type=part.part_type)
            parts_inventory.quantity = parts_inventory.quantity - part.part_quantity
            parts_inventory.save()
            data[part.part_type.name] = part.part_quantity
        return Response(data)
    
class BomDisplay(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        ref_part = PartType.objects.all()
        station = Station.objects.get(name='Warehouse')
        unit = UnitType.objects.get(name=station.instruction)
        parts = UnitPartsBom.objects.filter(unit_type=unit)
        data = {}
        for part in ref_part:
            data[part.name] = 0
        for part in parts:
            parts_inventory = PartsInventory.objects.get(part_type=part.part_type)
            parts_inventory.quantity = parts_inventory.quantity - part.part_quantity
            parts_inventory.save()
            data[part.part_type.name] = part.part_quantity
        return Response(data)

def assy1(request):
    return render(request, 'assy1.html')

class Assy1Instruction(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        station = Station.objects.get(name='Assembly 1')
        return Response({"img": station.instruction})
        
    def post(self, request):
        product_code = request.data['product_code']
        product = Products.objects.get(product_code=product_code)
        product.time_assy1 = datetime.datetime.now()
        product.save()
        unit_type = product.unit_type.name
        if unit_type == "X":
            station = Station.objects.get(name='Assembly 1')
            station.instruction = '/media/X_assy1.png'
            station.save()
            return Response({"msg": "success"})
        elif unit_type == "Y":
            station = Station.objects.get(name='Assembly 1')
            station.instruction = '/media/Y_assy1.png'
            station.save()
            return Response({"msg": "success"})
        elif unit_type == "Z":
            station = Station.objects.get(name='Assembly 1')
            station.instruction = '/media/Z_assy1.png'
            station.save()
            return Response({"msg": "success"})

def assy2(request):
    return render(request, 'assy2.html')

class Assy2Instruction(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        station = Station.objects.get(name='Assembly 2')
        return Response({"img": station.instruction})
        
    def post(self, request):
        product_code = request.data['product_code']
        product = Products.objects.get(product_code=product_code)
        product.time_assy2 = datetime.datetime.now()
        product.save()
        unit_type = product.unit_type.name
        if unit_type == "X":
            station = Station.objects.get(name='Assembly 2')
            station.instruction = '/media/X_assy2.png'
            station.save()
            return Response({"msg": "success"})
        elif unit_type == "Y":
            station = Station.objects.get(name='Assembly 2')
            station.instruction = '/media/Y_assy2.png'
            station.save()
            return Response({"msg": "success"})
        elif unit_type == "Z":
            station = Station.objects.get(name='Assembly 2')
            station.instruction = '/media/Z_assy2.png'
            station.save()
            return Response({"msg": "success"})

def inspection(request):
    return render(request, 'inspection.html')

class InspectionInstruction(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        station = Station.objects.get(name='Inspection')
        return Response({"img": station.instruction})
        
    def post(self, request):
        product_code = request.data['product_code']
        product = Products.objects.get(product_code=product_code)
        product.time_inspection = datetime.datetime.now()
        product.save()
        unit_type = product.unit_type.name
        if unit_type == "X":
            station = Station.objects.get(name='Inspection')
            station.instruction = '/media/X_inspection.png'
            station.save()
            return Response({"msg": "success"})
        elif unit_type == "Y":
            station = Station.objects.get(name='Inspection')
            station.instruction = '/media/Y_inspection.png'
            station.save()
            return Response({"msg": "success"})
        elif unit_type == "Z":
            station = Station.objects.get(name='Inspection')
            station.instruction = '/media/Z_inspection.png'
            station.save()
            return Response({"msg": "success"})

class StoreView(APIView):
    permission_classes = [AllowAny]
        
    def post(self, request):
        product_code = request.data['product_code']
        product = Products.objects.get(product_code=product_code)
        product.time_storage = datetime.datetime.now()
        product.save()
        unit_type = product.unit_type
        
        storage = UnitStorage.objects.get(unit_type=unit_type)
        storage.quantity += 1
        storage.save()
        
        storages = UnitStorage.objects.all()
        data = {}
        for i in storages:
            data[i.unit_type.name] = i.quantity
        return Response(data)
    
class DeliverView(APIView):
    permission_classes = [AllowAny]
        
    def post(self, request):
        product_code = request.data['product_code']
        product = Products.objects.get(product_code=product_code)
        product.time_delivered = datetime.datetime.now()
        product.save()
        unit_type = product.unit_type
        
        storage = UnitStorage.objects.get(unit_type=unit_type)
        storage.quantity -= 1
        storage.save()
        
        storages = UnitStorage.objects.all()
        data = {}
        for i in storages:
            data[i.unit_type.name] = i.quantity
        return Response(data)
    
class StorageView(APIView):
    permission_classes = [AllowAny]
        
    def get(self, request):
        storages = UnitStorage.objects.all()
        data = {}
        for i in storages:
            data[i.unit_type.name] = i.quantity
        return Response(data)

class LeadWarehouseView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        products = Products.objects.filter(time_assy1__isnull=False)
        total_product = len(products)
        total_warehouse_time = datetime.timedelta(seconds=0)
        print(total_product)
        for product in products:
            total_warehouse_time += product.time_assy1 - product.time_warehouse
        warehouse_time = total_warehouse_time/total_product
        return Response({"warehouse": warehouse_time.total_seconds()})

class LeadAssy1View(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        products = Products.objects.filter(time_assy2__isnull=False)
        total_product = len(products)
        total_assy1_time = datetime.timedelta(seconds=0)
        for product in products:
            total_assy1_time += product.time_assy1 - product.time_warehouse
        assy1_time = total_assy1_time/total_product
        return Response({"assy1": assy1_time.total_seconds()})

class LeadAssy2View(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        products = Products.objects.filter(time_storage__isnull=False)
        total_product = len(products)
        total_warehouse_time = datetime.timedelta(seconds=0)
        for product in products:
            total_warehouse_time = product.time_assy1 - product.time_warehouse
        warehouse_time = total_warehouse_time/total_product
        return Response({"assy2": warehouse_time.total_seconds()})

class LeadStorageView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        products = Products.objects.filter(time_delivered__isnull=False)
        total_product = len(products)
        total_warehouse_time = datetime.timedelta(seconds=0)
        for product in products:
            total_warehouse_time = product.time_assy1 - product.time_warehouse
        warehouse_time = total_warehouse_time/total_product
        return Response({"storage": warehouse_time.total_seconds()})

class LeadProductionView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        products = Products.objects.filter(time_delivered__isnull=False)
        total_product = len(products)
        total_warehouse_time = datetime.timedelta(seconds=0)
        for product in products:
            total_warehouse_time = product.time_delivered - product.time_warehouse
        warehouse_time = total_warehouse_time/total_product
        return Response({"lead_time": warehouse_time.total_seconds()})

        