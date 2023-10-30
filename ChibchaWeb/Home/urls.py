from django.urls import path
from .views import acercaDeNos, home, planes, inicioSesion, registro_clientes, dashboard_view, singout, eliminar_usuario

urlpatterns = [
    path("", home, name='home'),
    path("acercaDeNosotros", acercaDeNos, name='acercaDeNosotros'),
    path("planes", planes, name='planes'),
    path("signin", inicioSesion, name="inicioSesion"),
    path("signout", singout, name="cerrarSesion"),
    path("registro", registro_clientes, name="registroCliente"),
    path("eliminar", eliminar_usuario, name="eliminarUsuario"),
    path("dashboard", dashboard_view, name="dashboard"),
]