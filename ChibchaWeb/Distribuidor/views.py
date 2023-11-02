from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Distribuidor

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