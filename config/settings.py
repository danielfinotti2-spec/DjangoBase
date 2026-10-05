"""Configurações do projeto Django.

Consulte a documentação para entender as opções disponíveis:
https://docs.djangoproject.com/en/6.1/topics/settings/
"""

from pathlib import Path

# Define caminhos do projeto, como BASE_DIR / 'subdiretorio'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Configurações iniciais de desenvolvimento; revise-as antes de publicar em produção.
# Consulte https://docs.djangoproject.com/en/6.1/howto/deployment/checklist/

# AVISO DE SEGURANÇA: mantenha secreta a chave usada em produção.
SECRET_KEY = '[REDACTED]'

# AVISO DE SEGURANÇA: não deixe a depuração ativada em produção.
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']



# Aplicativos e componentes instalados no projeto.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cadastro',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Aponta para o arquivo que declara as rotas principais do projeto.
ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Banco de dados usado pelo projeto (SQLite, armazenado em um arquivo local).
# https://docs.djangoproject.com/en/6.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Validadores aplicados às senhas criadas pelos usuários.
# https://docs.djangoproject.com/en/6.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Idioma, fuso horário e suporte à internacionalização.
# https://docs.djangoproject.com/en/6.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Caminho usado para servir arquivos estáticos, como CSS, JavaScript e imagens.
# https://docs.djangoproject.com/en/6.1/howto/static-files/

STATIC_URL = 'static/'


# Configuração de e-mail: neste projeto, as mensagens são exibidas no console.
# https://docs.djangoproject.com/en/6.1/topics/email/#topic-email-configuration

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Redireciona usuários sem sessão para a página de entrada do Django.
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'
