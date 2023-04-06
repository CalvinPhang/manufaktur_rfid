from django.contrib import admin
from .models import RFID

@admin.register(RFID)
class RFIDAdmin(admin.ModelAdmin):
    list_display = ("id", "reader_id", "content", "timestamp")
# Register your models here.
