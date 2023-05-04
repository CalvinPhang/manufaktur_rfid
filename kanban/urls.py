from django.urls import path

from . import views

urlpatterns = [
    path('order', views.order_input),
    path('order/input', views.OrderPost.as_view()),
    path('bom', views.BomProduct.as_view()),
    
    path('assy1', views.assy1),
    path('assy1/img', views.Assy1Instruction.as_view()),
    
    path('assy2', views.assy2),
    path('assy2/img', views.Assy2Instruction.as_view()),
    
    path('inspection', views.inspection),
    path('inspection/img', views.InspectionInstruction.as_view()),
    
    path('storage', views.StorageView.as_view()),
]