"""Configuração WSGI do projeto Django.

Expõe o objeto ``application``, usado por servidores compatíveis com WSGI.
Consulte https://docs.djangoproject.com/en/6.1/howto/deployment/wsgi/.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Cria a aplicação WSGI com as configurações definidas pelo projeto.
application = get_wsgi_application()
