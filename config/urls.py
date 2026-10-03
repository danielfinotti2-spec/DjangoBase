"""Rotas de acesso do projeto Django.

A lista urlpatterns associa endereços a páginas ou funcionalidades.
Consulte https://docs.djangoproject.com/en/6.1/topics/http/urls/ para mais detalhes.
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/', include('django.contrib.auth.urls')),
    path('', include('cadastro.urls')),
]

# Define a página exibida quando nenhuma rota corresponde ao endereço.
handler404 = 'cadastro.views.handler404'
