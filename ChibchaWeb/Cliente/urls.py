from django.urls import path
from .views import consulta_cliente, consulta_clientes, registro_clientes, editarCliente, eliminar_cliente, ingresar, dashboard_view, inicioSesion

urlpatterns = [
    path("", consulta_clientes, name='consultaClientes'),
    path("editar", editarCliente, name='editarCliente'),
    path("prueba", consulta_cliente, name='consultaCliente'),
    path("registro", registro_clientes, name='registroCliente'),
    path("inicioSesion", inicioSesion, name='inicioSesion'),
    path("ingreso", ingresar, name='ingresar'),
    path("<int:id_cliente>/delete", eliminar_cliente, name='eliminarCliente'),
    path('dashboard', dashboard_view, name='dashboard'),
]