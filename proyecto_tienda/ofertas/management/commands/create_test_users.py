"""#crear usuarios de prueba con sus contraseñas, permisos y grupos
from django.contrib.auth.models import User, Group, Permission
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help= 'Crea usuario de prueba para la aplicación y asigna permisos'
    
    def asignar_permisos_grupo(self, grupo_nombre, permisos):
        grupo, creado= Group.objects.get_or_create(name=grupo_nombre) #el creado no se usa en este momento
        for permiso in permisos:
            grupo.permissions.add(Permission.objects.get(codename=permiso))#asocia los permisos a ese grupo
            
    def handle(self, *args, **kwargs):
        #verificando y creando el usuario admin (si no existiera lo crea)
        admin_user, created = User.objects.get_or_create(
            username='Admin',
            defaults={'email': 'admin@admin.cl', 'is_staff': True},
        )
        if created: 
            admin_user.set_password('adminpass')
            admin_user.is_active= True
            admin_user.save()
            
        #verificando y creando el usuario editor
        editor_user, created = User.objects.get_or_create(
            username='Editor',
            defaults={'email': 'editor@editor.cl'},
        )
        if created: 
            editor_user.set_password('editorpass')
            editor_user.is_active= True
            editor_user.save()
            
        #verificando y creado el usuario invitado
        guest_user, created = User.objects.get_or_create(
            username='Guest',
            defaults={'email': 'guest@guest.cl'},
        )
        if created: 
            guest_user.set_password('guestpass')
            guest_user.is_active= True
            guest_user.save()
            
        #Asignar permisos para los grupos
        self.asignar_permisos_grupo('Admin', ['add_oferta', 'change_oferta', 'delete_oferta', 'view_oferta'])
        self.asignar_permisos_grupo('Editor', ['add_oferta', 'view_oferta'])
        self.asignar_permisos_grupo('Guest', ['view_oferta'])
        
        try:
            admin_group = Group.objects.get('Admin')
            editor_group= Group.objects.get('Editor')
            guest_group= Group.objects.get('Guest')
            
            admin_user.groups.add(admin_group)
            editor_user.groups.add(editor_group)
            guest_user.groups.add(guest_group)
        except Group.DoesNotExist:
            self.stdout.write(self.style.WARNING("Los grupos no existen. Asegúrate de que los grupos 'Admin', 'Editor' y 'Guest' existan"))
            self.stdout.write(self.style.SUCCESS('Usuarios y permisos creados exitosamente'))"""
            
"""from typing import Any
from django.contrib.auth.models import User, Group, Permission
from django.core.management.base import BaseCommand
 
class Command(BaseCommand):
    help = 'Crea usuarios de prueba para la aplicacion y asigna permisos a grupos'
 
    def asignar_permisos_grupo(self, grupo_nombre, permisos):
        grupo, creado = Group.objects.get_or_create(name=grupo_nombre)
 
        for permiso in permisos:
            grupo.permissions.add(Permission.objects.get(codename=permiso))
 
    def handle(self, *args, **kwargs):
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults= {'email': 'admin@admin.cl', 'is_staff' : True},
        )
 
        #Verificado y creando el usuario admin
        if created:
            admin_user.set_password('adminpass')
            admin_user.is_active=True
            admin_user.save()
 
        #Verificado y creando el usuario editor
 
        editor_user, created = User.objects.get_or_create (
            username='editor',
            defaults= {'email': 'editor@admin.cl'},
        )
       
       
        if created:
            editor_user.set_password('editiarpass')
            editor_user.is_active=True
            editor_user.save()
 
        #Verificado y creando el usuario guest
        guest_user, created = User.objects.get_or_create (
            username='guest',
            defaults= {'email': 'guest@admin.cl'},
        )
       
        if created:
            guest_user.set_password('guestpass')
            guest_user.is_active=True
            guest_user.save()
 
 
        #Asignando permiso a los grupos
        self.asignar_permisos_grupo('Admin', ['add_oferta', 'delete_oferta', 'change_oferta', 'view_oferta'])
        self.asignar_permisos_grupo('Editor',['add_oferta', 'view_oferta'])
        self.asignar_permisos_grupo('Guest', ['view_oferta'])
 
        try:
            admin_group = Group.objects.get('Admin')
            editor_group = Group.objects.get('Editor')
            guest_group = Group.objects.get('Guest')
 
            admin_user.groups.add(admin_group)
            editor_user.groups.add(editor_group)
            guest_user.groups.add(guest_group)
       
        except Group.DoesNotExist:
            self.stdout.write(self.style.WARNING('Los grupos no existen. Asegurate de que los grupos Admin, Editor y Guest existan'))
       
        self.stdout.write(self.style.SUCCESS('Usuarios y permisos creados exitosamente'))"""
        
from django.contrib.auth.models import User, Group, Permission
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Crea usuarios de prueba para la aplicación y asigna permisos a grupos'

    def asignar_permisos_grupo(self, grupo_nombre, permisos):
        grupo, creado = Group.objects.get_or_create(name=grupo_nombre)
        for permiso in permisos:
            grupo.permissions.add(Permission.objects.get(codename=permiso))

    def handle(self, *args, **kwargs):
        # Verificar y crear el usuario 'admin' si no existe
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={'email': 'admin@example.com', 'is_staff': True}
        )
        if created:
            admin_user.set_password('adminpass')
            admin_user.is_active = True
            admin_user.save()

        # Verificar y crear el usuario 'editor' si no existe
        editor_user, created = User.objects.get_or_create(
            username='editor',
            defaults={'email': 'editor@example.com'}
        )
        if created:
            editor_user.set_password('editorpass')
            editor_user.is_active = True
            editor_user.save()

        # Verificar y crear el usuario 'guest' si no existe
        guest_user, created = User.objects.get_or_create(
            username='guest',
            defaults={'email': 'guest@example.com'}
        )
        if created:
            guest_user.set_password('guestpass')
            guest_user.is_active = True
            guest_user.save()

        # Asignar permisos a los grupos
        self.asignar_permisos_grupo('Admin', ['add_oferta', 'change_oferta', 'delete_oferta', 'view_oferta'])
        self.asignar_permisos_grupo('Editor', ['add_oferta', 'view_oferta'])
        self.asignar_permisos_grupo('Guest', ['view_oferta'])

        # Asignar usuarios a sus respectivos grupos si los grupos existen
        try:
            admin_group = Group.objects.get(name='Admin')
            editor_group = Group.objects.get(name='Editor')
            guest_group = Group.objects.get(name='Guest')

            admin_user.groups.add(admin_group)
            editor_user.groups.add(editor_group)
            guest_user.groups.add(guest_group)
        except Group.DoesNotExist:
            self.stdout.write(self.style.WARNING("Asegúrate de que los grupos 'Admin', 'Editor', y 'Guest' existan."))

        self.stdout.write(self.style.SUCCESS('Usuarios y permisos configurados correctamente.'))