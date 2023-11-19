from datetime import date, datetime
from abc import ABC, abstractmethod
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from Distribuidor.models import Distribuidor
from Cliente.models import Archivo, Cliente, TarjetaCredito, Dominio, SitioWeb

class ReportGenerator(ABC):
    @abstractmethod
    def generar_rep(self, distribuidor, cliente):
        pass

class PDFReportGenerator(ReportGenerator):
    
    def generar_rep(self, distribuidor, clientes):
        ancho_pagina = 841.89
        alto_pagina = 595.27 
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="reporte_contratos.pdf"'

        p = canvas.Canvas(response)
        p.setPageSize((ancho_pagina, alto_pagina))
        p.setFillColorRGB(221/255,238/255,239/255)
        p.rect(0,0,ancho_pagina,alto_pagina,fill=1)
        p.setFillColorRGB(0,0,0)
        p.setTitle(f'Reporte de Contratos {distribuidor.nombreDistribuidor}')
        p.setFont('Helvetica', 12)
        #pdf.setFont('abc',tamaño)
        #pdf.setFillColorRGB(0,0,0)
        p.drawString(ancho_pagina - 80, alto_pagina - 20, date.today().strftime("%d/%m/%Y"))
        p.drawString(ancho_pagina - 80, alto_pagina - 40, datetime.now().strftime("%H:%M:%S"))
        p.drawInlineImage("chibchaweb_django\static\images\logo.jpg", 390-ancho_pagina, alto_pagina - 60, preserveAspectRatio=True, height=50)
        p.drawString(90, alto_pagina - 40, 'CibchaWeb')
        p.drawCentredString(ancho_pagina / 2, alto_pagina - 85, f'Reporte de Contratos para {distribuidor.nombreDistribuidor}')
       

        y_position = 780
        for cliente in clientes:
            y_position -= 20
            p.drawString(
                100,
                y_position,
                f'Cliente: {cliente.nombreCliente}, Nombre del dominio: {cliente.dominio.nombreDomino}'
            )

            

        p.showPage()
        p.save()

        return response
