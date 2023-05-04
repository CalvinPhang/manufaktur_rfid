from django.urls import path

from . import views

urlpatterns = [
    path('order', views.order_input),
    path('order/input', views.OrderPost.as_view()),
    path('bom', views.BomProduct.as_view())
]