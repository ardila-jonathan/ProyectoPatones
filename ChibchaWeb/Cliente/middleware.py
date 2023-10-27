from typing import Any
from django.shortcuts import render, redirect

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response=get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    '''def process_request(self, request):
        # Comprobar si el usuario está autenticado
        if not request.user.is_authenticated:
            # Redirigir al usuario a la página de inicio de sesión
            return redirect('inicioSesion')'''