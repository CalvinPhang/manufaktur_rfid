from django.urls import path

from . import views

urlpatterns = [
    path('order', views.order_input),
    path('order/input', views.OrderPost.as_view()),
    
    path('bom', views.BomProduct.as_view()),
    path('bom/display', views.BomDisplay.as_view()),
    
    path('assy1', views.assy1),
    path('assy1/img', views.Assy1Instruction.as_view()),
    
    path('assy2', views.assy2),
    path('assy2/img', views.Assy2Instruction.as_view()),
    
    path('inspection', views.inspection),
    path('inspection/img', views.InspectionInstruction.as_view()),
    
    path('store', views.StoreView.as_view()),
    path('deliver', views.DeliverView.as_view()),
    path('storage', views.StorageView.as_view()),
    
    path('warehouse-time', views.LeadWarehouseView.as_view()),
    path('assy1-time', views.LeadAssy1View.as_view()),
    path('assy2-time', views.LeadAssy2View.as_view()),
    path('storage-time', views.LeadStorageView.as_view()),
    path('total-time', views.LeadProductionView.as_view()),
]