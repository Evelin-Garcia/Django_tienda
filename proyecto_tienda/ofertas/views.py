from datetime import datetime
from django.shortcuts import render, redirect
from .models import Oferta
from .forms import OfertaForm

# Create your views here.

#funcion para el formulario de ofertas
def crear_oferta(request):
    if request.method=='POST':
        form=OfertaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ofertas:index')
    else:
        form=OfertaForm()
    return render(request, 'ofertas/crear_oferta.html', {'form':form})
    

def index(request):
    current_date=datetime.now()
    ofertas=[]
    
    try:
        ofertas=Oferta.objects.filter(fecha_inicio__lte=current_date, fecha_fin__gte=current_date) 
#        raise Exception("Simulación de error inesperado")  #Esta línea se hizo para probar que el error inesperado del bloque try except está funcionando, debe mantenerse comentada.
        if not ofertas:
            raise ValueError("No hay ofertas disponibles en este momento")
    except ValueError as e:
        #Manejo de error específico (no hay ofertas)
        return render(request, 'ofertas/index.html', {'error': str(e), 'current_date': current_date})
    except Exception as e:
        #Manejo de cualquier otro error
        return render(request, 'ofertas/index.html', {'error': 'Se produjo un error inesperado!', 'current_date': current_date})
    
    context={
#        'is_special_offer': False  #Se Cambia a True para si y False para no (para que aparezca si o no)        
        'current_date':current_date,
        'ofertas':ofertas
    }
    return render(request, 'ofertas/index.html', context)