from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import PessoaForm

from django.http import HttpResponse

def listar_pessoas(request):
        pessoas = Pessoa.objects.all()
        return render(request, 'meuapp/list.html', {'pessoas': pessoas})

def criar_pessoas(request):
        if request.method == 'POST':
            form = PessoaForm(request.POST)

            if form.is_valid():
                   form.save()
                   return redirect('listar_pessoas')
        else:
            form = PessoaForm()
        return render(request, 'meuapp/forms.html', {'form': form})

def atualizar_pessoa(request, pk):
    pessoa = Pessoa.objects.get(pk=pk)

    if request.method == "POST":
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'meuapp/forms.html', {'form': form})
def deletar_pessoa(request, pk):
        pessoa = Pessoa.objects.get(pk=pk)
        if request.method =="POST":
                pessoa.delete()
                return redirect('listar_pessoas')
        return render(request, 'meuapp/confirmar_delete.html', {'pessoa': pessoa})


# Create your views here.
