from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PessoaForm
from .models import Pessoa


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
