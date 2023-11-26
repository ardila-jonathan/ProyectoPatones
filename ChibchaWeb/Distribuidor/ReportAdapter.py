from .ReportFacade import ReportFacade
from Distribuidor.models import Distribuidor

class TargetInterface():

    @classmethod
    def getListData(cls, distribuidor:Distribuidor ):
        pass

class ReportAdapter(ReportFacade, TargetInterface):
    
    @classmethod
    def getListData(cls, distribuidor:Distribuidor):
        dd = ReportFacade.getDictData(distribuidor)
        data = []

        for dictionary in dd[:-3]:
            data_item = []
            for key in dictionary:
                data_item.append(dictionary[key])

            data.append(data_item)
        
        data.extend(dd[-3:])
        return data
