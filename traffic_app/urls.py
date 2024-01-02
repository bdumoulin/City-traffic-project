from django.urls import path
from .views import map_view, calculate_best_way

urlpatterns = [
    path('map/', map_view, name='map_view'),
    path('way/', calculate_best_way, name='calculate_best_way'),
]
