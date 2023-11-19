from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .ReporteContrato import PDFReportGenerator	
from Cliente.models import Cliente
from .models import Distribuidor
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

def descargarReporteContrato(request):
    generador = PDFReportGenerator()
    distribuidor = Distribuidor.objects.get(usuario=request.user)  
    clientes_con_dominio = Cliente.objects.filter(
    dominio__extencionDominio__distribuidor_extensiondominio=distribuidor
        ).distinct
   
    response = generador.generar_rep(distribuidor, clientes_con_dominio)

    return response