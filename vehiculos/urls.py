from django.urls import path
from vehiculos.views import index, VehiculosListView

urlpatterns = [
    path('', index(), name='index'),
    path('vehiculo/add', datosform_view, name='datosform'),
]