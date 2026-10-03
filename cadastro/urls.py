from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('contas/cadastro/', views.signup, name='signup'),
    path('pessoas/adicionar/', views.adicionar, name='adicionar'),
    path('pessoas/<int:id>/', views.detalhe, name='detalhe'),
    path('pessoas/<int:id>/editar/', views.editar, name='editar'),
    path('pessoas/<int:id>/deletar/', views.deletar, name='deletar'),
]
