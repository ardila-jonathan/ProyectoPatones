from .models import Distribuidor, ExtensionDominio
from Cliente.models import Cliente, TarjetaCredito, Dominio

class ReportFacade:
    
    @classmethod
    def getDictData(cls, distribuidor):
        dominiosDistribuidor = []
        extensionesDistribuidor = ExtensionDominio.objects.filter(distribuidorId = distribuidor)
        data = []

        if extensionesDistribuidor:
            for dominio in Dominio.objects.all():
                try:
                    if dominio.extensionDominio in extensionesDistribuidor:
                        dominiosDistribuidor.append(dominio)
                except:
                    pass

            total = 0
            total_comision = 0
            for dominio in dominiosDistribuidor:
                tarjeta = TarjetaCredito.objects.get(clienteId = dominio.clienteId)
                data.append({'nombreDom':dominio.nombreDominio,
                            'extension':dominio.extensionDominio.extensionDominio,
                            'nombreCli':dominio.clienteId.nombreCliente,
                            'valorCon':dominio.extensionDominio.precioExtension,
                            'comision':(distribuidor.comision/100)*dominio.extensionDominio.precioExtension,
                            'tarjeta':tarjeta.numeroTarjeta}) 
                
                total += data[len(data)-1]['valorCon']
                total_comision += data[len(data)-1]['comision']
                
            data.append(total)
            data.append(total_comision)
            data.append(total-total_comision)
        
        return data