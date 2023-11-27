from django.shortcuts import render

from aplicacaoAppadaria.forms import pedidoForms

from aplicacaoAppadaria.models import FilaCliente

from datetime import date

def index(request):
    return render(request, 'index.html')  

def pedido(request):
        form = pedidoForms()
        return render(request, 'pedido.html', {"form": form})

from django.shortcuts import render, redirect
from aplicacaoAppadaria.forms import pedidoForms
from aplicacaoAppadaria.models import FilaCliente
from datetime import date
from django.core.serializers import serialize

def fila(request):
    data = date.today()
    if request.method == 'GET':
        form = pedidoForms(request.GET)

        if form.is_valid():
            quantidade = form.cleaned_data["quantidade_forms"]
            nome = form.cleaned_data["nome_login"]
            data = date.today()

            filaCliente = FilaCliente(nome=nome, quantidade=quantidade, data=data)
            filaCliente.save()

    if data is not None:  
        dados_filtrados = FilaCliente.objects.filter(data=data)
        dados_ordenados = dados_filtrados.order_by('id', 'data')
        lista_dados = [[item.nome, item.quantidade] for item in dados_ordenados]

        dados_fila_json = serialize('json', dados_ordenados)

        return render(request, 'fila.html', {'lista_dados': lista_dados, 'data': data, 'dados_fila_json': dados_fila_json})
    else:
        return render(request, 'fila.html', {'data': None, 'dados_fila_json': '[]'})



