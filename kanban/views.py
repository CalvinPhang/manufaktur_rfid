from django.shortcuts import render
import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Order, UnitType, PartsInventory, UnitPartsBom, Products

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
        print(parts)
        for part in parts:
            parts_inventory = PartsInventory.objects.get(part_type=part.part_type)
            if parts_inventory.quantity - part.part_quantity < 0:
                return Response({'msg': "Parts not sufficient"})
        for part in parts:
            parts_inventory = PartsInventory.objects.get(part_type=part.part_type)
            parts_inventory.quantity = parts_inventory.quantity - part.part_quantity
            parts_inventory.save()
        order = Order(
            id = dictt["ID"],
            product = unit,
            quantity = int(dictt["qt"]),
            order_date = datetime.datetime.now()
        )
        order.save()
        return Response({'msg': 'order received'})

