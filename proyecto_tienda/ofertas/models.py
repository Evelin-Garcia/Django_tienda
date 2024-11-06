from django.db import models
from productos.models import Producto

# Create your models here.

class Oferta(models.Model):
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    porcentaje_descuento=models.DecimalField(max_digits=5, decimal_places=2)
    fecha_inicio=models.DateTimeField()
    fecha_fin=models.DateTimeField()
    
    def __str__(self):
        return f"Oferta en {self.producto.nombre} - {self.porcentaje_descuento}% de descuento"
    
    @property
    def precio_oferta(self):
        return self.producto.precio*(1-(self.porcentaje_descuento/100))
    