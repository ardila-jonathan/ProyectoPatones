from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from datetime import date, datetime
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors

class BancaryReportGenerator:

    __instance = None
    ancho_pagina = 595.27
    alto_pagina = 841.89

    def __BancaryReportGenerator(self):
        #Constructor privado
        pass

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super(BancaryReportGenerator, cls).__new__(cls)

            """
            pdfmetrics.registerFont(
                TTFont('nombrefuente', 'ruta_fuente')
            )
            """
            print("No existe")
        else:
            print("Ya existe")

        return cls.__instance
    
    def generatePDF(cls, response, nombreDistribuidor, info:list):
        pdf = canvas.Canvas(response)
        pdf.setPageSize(( cls.ancho_pagina, cls.alto_pagina))
        pdf.setFillColorRGB(221/255,238/255,239/255)
        pdf.rect(0,0,cls.ancho_pagina,cls.alto_pagina,fill=1)
        pdf.setFillColorRGB(0,0,0)
        pdf.setTitle('Reporte Bancario ' + nombreDistribuidor)
        #pdf.setFont('abc',tamaño)
        #pdf.setFillColorRGB(0,0,0)
        pdf.drawString(cls.ancho_pagina - 80, cls.alto_pagina - 20, date.today().strftime("%d/%m/%Y"))
        pdf.drawString(cls.ancho_pagina - 80, cls.alto_pagina - 40, datetime.now().strftime("%H:%M:%S"))
        pdf.drawInlineImage("chibchaweb_django\static\images\logo.jpg", 130-cls.ancho_pagina, cls.alto_pagina - 60, preserveAspectRatio=True, height=50)
        pdf.drawString(80, cls.alto_pagina - 40, 'CibchaWeb')
        pdf.drawCentredString(cls.ancho_pagina / 2, cls.alto_pagina - 85, "Reporte Bancario " + nombreDistribuidor)

        #Agregar tabla
        data = [['Nombre dominio', 'Extensión dominio', 'Nombre Cliente', 'Valor Total Contrato', 'Valor Comisión', 'Tarjeta de Crédito'],]
        data.extend(info[:-3])
        table = Table(data, spaceBefore=20, spaceAfter=20)

        style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.Color(38/255, 239/255, 250/255)), 
        ('LINEABOVE', (0,1), (-1,-1), 1, colors.black),
        ('LINEBELOW', (0,-1), (-1,-1), 1, colors.black),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  
        ])

   
        for i in range(1, len(data)):
            if i % 2 == 0:
                bg_color = colors.white
            else:
                bg_color = colors.Color(186/255, 199/255, 199/255)
            style.add('BACKGROUND', (0, i), (-1, i), bg_color)

        table.setStyle(style)


        w, h = table.wrapOn(pdf, 0, 0)
        table.drawOn(pdf, cls.ancho_pagina/2 - w/2, cls.alto_pagina - h - 100) 

        print(info)
        y_position = cls.alto_pagina - h - 150 
        pdf.drawString(28, y_position, "Total mensual: COP " + str(int(info[-3])))
        pdf.drawString(28, y_position - 20, "Total comisión a ChibchaWeb: COP " + str(int(info[-2])))
        pdf.drawString(28, y_position - 40, "Total ingresos mensuales: COP " + str(int(info[-1]))) 

        pdf.showPage()
        pdf.save()

