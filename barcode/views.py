from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Barcode

def barcode_input(request):
    return render(request, 'barcode.html')

class barcode_post(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        obj = Barcode(
            content=request.data['content'],
        )
        obj.save()
        return Response({'msg': 'create success'})

