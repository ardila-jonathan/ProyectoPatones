from django.urls import path
from .views import consulta_cliente, consulta_clientes, editar_cliente, eliminar_cliente

urlpatterns = [
    path("", consulta_clientes, name='consultaClientes'),
    path("prueba", consulta_cliente, name='consultaCliente'),
    path("<int:id_cliente>/delete", eliminar_cliente, name='eliminarCliente'),
    path("<int:id_cliente>/modificar", editar_cliente, name='editarCliente')
    #path('dashboard', dashboard_view, name='dashboard'),
]