from django.urls import path
from .views import editar_distribuidor, descargarReporte, reporteContrato, registroExtension, vmodificarExtension, modificarPrecioExtension, solicitudXML
from Home.views import eliminar_usuario

urlpatterns = [
    path("<int:id_distribuidor>/modificar", editar_distribuidor, name='editarDistribuidor'),
    path("reporteBancario", descargarReporte, name="reporteBancario"),
    path("reporte_contrato/<str:dist>/", reporteContrato, name="reporteContrato"),
    path("registroExtension", registroExtension, name="registroExtension"),
    path("modExtension/<int:ext>", vmodificarExtension, name="modExtension"),
    path("actExtension", modificarPrecioExtension, name="actExtension"),
    path("solicitudXML/<int:dominioId>", solicitudXML, name="solicitudXML" ),
]