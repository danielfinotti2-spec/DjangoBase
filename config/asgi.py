"""Configuração ASGI do projeto Django.

Expõe o objeto ``application``, usado por servidores compatíveis com ASGI.
Consulte https://docs.djangoproject.com/en/6.1/howto/deployment/asgi/.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Cria a aplicação ASGI com as configurações definidas pelo projeto.
application = get_asgi_application()
