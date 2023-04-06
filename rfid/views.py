from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import RFID

class rfid_post(APIView):
    def post(self, request, *args, **kwargs):
        obj = RFID(
            reader_id=request.data['reader_id'],
            content=request.data['content'],
        )
        obj.save()
        return Response({'msg': 'create success'})
        
        
        
        