from django.urls import path

from . import views

urlpatterns = [
    path('', views.barcode_input),
    path('input', views.barcode_post.as_view())
]