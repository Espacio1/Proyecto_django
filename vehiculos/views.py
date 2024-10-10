from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from django.template import loader
from .forms import RegistroVehiculosForm
from .models import Vehiculo

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    context = {
        'Index': [
            {
                'title':'Catalogo de Vehiculos',
                'body':'Información disponible en breve',
            }
        ]
    }
    return HttpResponse(template.render({},request))

class VehiculosListView(ListView):
    model=Vehiculo
    template_name='index.html'
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Catalogo de Vehículos'
        return context

def datosform_view(request):
    template = loader.get_template('formulario.html')
    return HttpResponse(template.render({},request))

    # Crear una aplicación vehículo, la cual contiene las siguientes características: 
    # Marca: Fiat, Chevrolet, Ford y Toyota.
    # 20 caracteres como máximo, y por defecto Ford.
    # Modelo:
    # 100 caracteres como máximo.
    # Serial Carrocería:
    # 50 caracteres como máximo.
    # Serial Motor:
    # 50 caracteres como máximo.
    # Categoría: Particular, transporte y carga.
    # 20 caracteres como máximo, y por defecto Particular.
    # Precio.
    # Fecha de creación.
    # Fecha de modificación.
    # 
    # Crear un usuario super administrador del framework Django con username: admin y password:admin.
