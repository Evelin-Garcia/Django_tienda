#crear usuarios de prueba con sus contraseñas, permisos y grupos
from django.contrib.auth.models import User, Group, Permission
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help= 'Crea usuario de prueba para la aplicación y asigna permisos'
    
    def asignar_permisos_grupo(self, grupo_nombre, permisos):
        grupo, creado= Group.objects.get_or_create(name=grupo_nombre) #el creado no se usa en este momento
        for permiso in permisos:
            grupo.permissions.add(Permission.objects.get(codename=permiso))#asocia los permisos a ese grupo
            
        