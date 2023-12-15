from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.update_model_detail_view ),
    path('class_serializer/', views.updated_Data_view.as_view() ),
    path('class_serializer/detail/', views.updated_Single_Data_view.as_view() ),
    path('json_dumps_method/', views.Update_data_View.as_view())
    
]
