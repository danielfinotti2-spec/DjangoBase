"""Rotas de acesso do projeto Django.

A lista urlpatterns associa endereços a páginas ou funcionalidades.
Consulte https://docs.djangoproject.com/en/6.1/topics/http/urls/ para mais detalhes.
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'contas/password_reset/',
        auth_views.PasswordResetView.as_view(
            template_name='cadastro/password_reset_form.html',
            email_template_name='cadastro/password_reset_email.html',
            subject_template_name='cadastro/password_reset_subject.txt',
        ),
        name='password_reset',
    ),
    path(
        'contas/password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='cadastro/password_reset_done.html',
        ),
        name='password_reset_done',
    ),
    path(
        'contas/reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='cadastro/password_reset_confirm.html',
        ),
        name='password_reset_confirm',
    ),
    path(
        'contas/reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='cadastro/password_reset_complete.html',
        ),
        name='password_reset_complete',
    ),
    path('contas/', include('django.contrib.auth.urls')),
    path('', include('cadastro.urls')),
]

# Define a página exibida quando nenhuma rota corresponde ao endereço.
handler404 = 'cadastro.views.handler404'
