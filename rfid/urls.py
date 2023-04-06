from django.urls import path

from . import views

urlpatterns = [
    path('rfid', views.rfid_post.as_view()),
]