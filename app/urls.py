from django.urls import path
from .views import index, informacion, galeria, formulario, api, productos, agregarrec, agregar, eliminar, actualizar, actualizarrec

urlpatterns = [
    path('', index, name='index'),
    path('informacion/', informacion, name='informacion'),
    path('galeria/', galeria, name='galeria'),
    path('formulario/', formulario, name='formulario'),
    path('api/', api, name='api'),

    path('productos/', productos, name='productos'),
    path('agregar/', agregar, name='agregar'),
    path('agregarrec/', agregarrec, name='agregarrec'),
    path('eliminar/<int:id>/', eliminar,name='eliminar'),
    path('actualizar/<int:id>/', actualizar,name='actualizar'),
    path('actualizar/actualizarrec/<int:id>/', actualizarrec,name='actualizarrec'),

    
]