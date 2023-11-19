from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .ReporteContrato import PDFReportGenerator	
from Cliente.models import Cliente, Dominio
from .models import Distribuidor, ExtensionDominio
from .GenRepBanc import BancaryReportGenerator

from django.http import HttpResponse
from .ReportAdapter import ReportAdapter


# Create your views here.
@login_required
def editar_distribuidor(request, id_distribuidor):
    
    user = request.user
    if user.id == id_distribuidor:
        if request.method == 'POST':
            
            distr = Distribuidor.objects.get(usuario_id = id_distribuidor)
            distr.nombreDistribuidor = request.POST['nombre']
            distr.categoria = request.POST['categoria']
            
            distr.save()
            return redirect('dashboard')
    else:
        return redirect('home')
    return render(request, "editarDistribuidor.html", {'distribuidor':Distribuidor.objects.get(usuario_id = id_distribuidor)})


def descargarReporte(request):
    generador = BancaryReportGenerator()
    distribuidor = Distribuidor.objects.get(usuario=request.user)  
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'
    generador.generatePDF(response, distribuidor.nombreDistribuidor,ReportAdapter.getListData(distribuidor))

    return response

def reporteContrato(request, dist):
    
    extensiones_dist = ExtensionDominio.objects.filter(distribuidorId_id=dist)
    
    dominios_dist = Dominio.objects.filter(extensionDominio__in=extensiones_dist)
    
    clientes_con_dominios_dist = Cliente.objects.filter(dominio__in=dominios_dist).distinct()
    print("asdasda")
    datos_clientes = []
    # Iterar sobre los clientes
    for cliente in clientes_con_dominios_dist:
        # Obtener los dominios asociados a cada cliente
        dominios_cliente = Dominio.objects.filter(clienteId_id=cliente,extensionDominio__in=extensiones_dist )

        # Almacenar los datos en un diccionario
        datos_cliente = {
            'cliente': cliente,
            'dominio': dominios_cliente
        }

        # Agregar el diccionario a la lista
        datos_clientes.append(datos_cliente)

    for dato_cliente in datos_clientes:
        for dominio in dato_cliente['dominio']:
            extension_dominio_id = dominio.extensionDominio_id
            distribuidor_extensiondominio = ExtensionDominio.objects.filter(extensionId=extension_dominio_id).first()
            dominio.distribuidor_extensiondominio = distribuidor_extensiondominio
    # Pasar la lista de datos_clientes a la plantilla

    return render(request, "repContratos.html", {'distribuidor':Distribuidor.objects.get(distribuidorId = dist), 'datos_clientes': datos_clientes})