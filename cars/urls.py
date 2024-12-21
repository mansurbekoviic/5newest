from django.urls import path
from . import views

urlpatterns = [
    path('brands/', views.brand_list, name='brand_list'),
    path('cars/<int:brand_id>/', views.car_list, name='car_list'),
]
