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
            form = PessoasForm()
        return render(request, 'meuapp/forms.html')

# Create your views here.
