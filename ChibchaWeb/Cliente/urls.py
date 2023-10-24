from django.urls import path
from .views import consulta_clientes, registro_clientes, eliminar_cliente

urlpatterns = [
    path("", consulta_clientes, name='consultaClientes'),
    path("registro", registro_clientes, name='registroCliente'),
    path("<int:id_cliente>/delete", eliminar_cliente, name='eliminarCliente'),
]