from django.urls import path
from . import views

app_name='productos'

urlpatterns= [
#    path('', views.index, name='productos_index'),
    path('', views.index, name='index'),
]