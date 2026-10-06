from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PessoaForm
from .models import Pessoa


def signup(request):
    """Cria uma conta comum e inicia a sessão do novo usuário."""
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        usuario = form.save()
        login(request, usuario)
        messages.success(request, 'Sua conta foi criada. Você já está conectado.')
        return redirect('index')
    return render(request, 'registration/signup.html', {'form': form})

def termos(request):
    """Exibe os termos de uso do projeto."""
    return render(request, 'cadastro/termos.html')


def politica(request):
    """Exibe a política de privacidade do projeto."""
    return render(request, 'cadastro/politica.html')


def sobre(request):
    """Exibe informações sobre o projeto."""
    return render(request, 'cadastro/sobre.html')


def index(request):
    """Mostra as pessoas cadastradas, com busca opcional por nome ou e-mail."""
    termo = request.GET.get('q', '').strip()
    pessoas = Pessoa.objects.all()
    if termo:
        pessoas = pessoas.filter(nome__icontains=termo) | pessoas.filter(email__icontains=termo)
    return render(request, 'cadastro/index.html', {'pessoas': pessoas, 'termo': termo})


def contato(request):
    """Exibe as informações de contato do projeto."""
    return render(request, 'cadastro/contato.html')


@login_required
def adicionar(request):
    """Valida e salva uma nova pessoa enviada pelo formulário."""
    form = PessoaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        pessoa = form.save()
        messages.success(request, f'{pessoa.nome} foi cadastrada com sucesso.')
        return redirect('detalhe', id=pessoa.id)
    return render(request, 'cadastro/formulario.html', {'form': form, 'titulo': 'Cadastrar pessoa'})


@login_required
def detalhe(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    return render(request, 'cadastro/detalhe.html', {'pessoa': pessoa})

@login_required
def ajuda(request):
    """Exibe a página de ajuda do projeto."""
    return render(request, 'cadastro/ajuda.html')

@login_required
def editar(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Cadastro atualizado com sucesso.')
        return redirect('detalhe', id=pessoa.id)
    return render(request, 'cadastro/formulario.html', {
        'form': form,
        'titulo': f'Editar {pessoa.nome}',
        'pessoa': pessoa,
    })


@login_required
def deletar(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == 'POST':
        nome = pessoa.nome
        pessoa.delete()
        messages.success(request, f'O cadastro de {nome} foi removido.')
        return redirect('index')
    return render(request, 'cadastro/deletar.html', {'pessoa': pessoa})


def handler404(request, exception):
    """Exibe uma página personalizada quando uma rota não existe."""
    return render(request, 'cadastro/404.html', status=404)
