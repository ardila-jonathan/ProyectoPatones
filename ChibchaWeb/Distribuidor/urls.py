from django.urls import path
from .views import editar_distribuidor, descargarReporte
from Home.views import eliminar_usuario

urlpatterns = [
    path("<int:id_distribuidor>/modificar", editar_distribuidor, name='editarDistribuidor'),
    path("reporteBancario", descargarReporte, name="reporteBancario"),
]