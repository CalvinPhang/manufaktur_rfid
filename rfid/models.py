from django.db import models

class RFID(models.Model):
    reader_id = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
