from django.shortcuts import render
import datetime
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Order, UnitType, PartsInventory, UnitPartsBom, Products, Station

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
        for part in parts:
            parts_inventory = PartsInventory.objects.get(part_type=part.part_type)
            parts_inventory.quantity = parts_inventory.quantity - part.part_quantity
            parts_inventory.save()
            
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
        parts = UnitPartsBom.objects.filter(unit_type=product.unit_type)
        data = {}
        for part in parts:
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
        unit_type = product.unit_type.name
        if unit_type == "X":
            station = Station.objects.get(name='Assembly 1')
            station.instruction = settings.ASSET_ROOT + 'X_assy1.png'
            station.save()
            return Response({"msg": "success"})
        elif unit_type == "Y":
            station = Station.objects.get(name='Assembly 1')
            station.instruction = settings.ASSET_ROOT + 'Y_assy1.png'
            station.save()
            return Response({"msg": "success"})
        elif unit_type == "Z":
            station = Station.objects.get(name='Assembly 1')
            station.instruction = settings.ASSET_ROOT + 'Z_assy1.png'
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
        unit_type = product.unit_type.name
        if unit_type == "X":
            station = Station.objects.get(name='Assembly 2')
            station.instruction = settings.ASSET_ROOT + 'X_assy2.png'
            station.save()
            return Response({"msg": "success"})
        elif unit_type == "Y":
            station = Station.objects.get(name='Assembly 2')
            station.instruction = settings.ASSET_ROOT + 'Y_assy2.png'
            station.save()
            return Response({"msg": "success"})
        elif unit_type == "Z":
            station = Station.objects.get(name='Assembly 2')
            station.instruction = settings.ASSET_ROOT + 'Z_assy2.png'
            station.save()
            return Response({"msg": "success"})
        


# class Assy2Instruction(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         product_code = request.data['product_code']
#         product = Products.objects.get(product_code=product_code)
#         unit_type = product.unit_type.name
#         if unit_type == "X":
#             return render(request, 'ProductX.html')
#         elif unit_type == "Y":
#             return render(request, 'ProductY.html')
#         elif unit_type == "Z":
#             return render(request, 'ProductZ.html')