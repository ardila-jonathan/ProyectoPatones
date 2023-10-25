from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")

def acercaDeNos(request):
    return render(request, "acercaDeNos.html")

def planes(request):
    return render(request, "planes.html")