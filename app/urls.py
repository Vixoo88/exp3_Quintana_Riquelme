from django.urls import path
from .views import index, informacion, galeria, formulario, api

urlpatterns = [
    path('', index, name='index'),
    path('informacion/', informacion, name='informacion'),
    path('galeria/', galeria, name='galeria'),
    path('formulario/', formulario, name='formulario'),
    path('api/', api, name='api'),
]