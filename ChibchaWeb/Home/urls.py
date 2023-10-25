from django.urls import path
from .views import acercaDeNos, home, planes

urlpatterns = [
    path("", home, name='home'),
    path("acercaDeNosotros", acercaDeNos, name='acercaDeNosotros'),
    path("planes", planes, name='planes'),
]