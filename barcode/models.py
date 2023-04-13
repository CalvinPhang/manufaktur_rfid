from django.db import models

class Barcode(models.Model):
    content = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
