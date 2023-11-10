from django.urls import path
from .views import consulta_cliente, consulta_clientes, editar_cliente, cambiar_tarjeta, registrarDominio, dominiosDisponibles, agregarPagina

urlpatterns = [
    #path("", consulta_clientes, name='consultaClientes'),
    #path("prueba", consulta_cliente, name='consultaCliente'),
    #path("<int:id_cliente>/delete", eliminar_cliente, name='eliminarCliente'),
    path("<int:id_cliente>/modificar", editar_cliente, name='editarCliente'),
    path("medioPago",cambiar_tarjeta, name = 'cambiarTarjeta'),
    path("registrarDominio", registrarDominio, name='registrarDominio'),
    path("dominiosDisponibles/<str:dominio>", dominiosDisponibles, name='dominiosDisponibles'),
    path("<int:id_cliente>/registrarPagina", agregarPagina, name='registrarPagina'),
    #path('dashboard', dashboard_view, name='dashboard'),
]