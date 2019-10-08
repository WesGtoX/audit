from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    template_name = 'licitacao/index.html'
    context = {}
    return render(request, template_name, context)


def licitacoes(request):
    template_name = 'licitacao/licitacoes.html'
    context = {}
    return render(request, template_name, context)


def aviso(request):
    template_name = 'licitacao/aviso.html'
    context = {}
    return render(request, template_name, context)


def julgamento(request):
    template_name = 'licitacao/julgamento.html'
    context = {}
    return render(request, template_name, context)


def homologada(request):
    template_name = 'licitacao/homologada.html'
    context = {}
    return render(request, template_name, context)


def denuncia(request):
    template_name = 'licitacao/denuncia.html'
    context = {}
    return render(request, template_name, context)


def obrigado(request):
    template_name = 'licitacao/obrigado.html'
    context = {}
    return render(request, template_name, context)
