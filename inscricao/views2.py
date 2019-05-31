# --*-- coding: uft-8 -*-
#from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .forms import *
from .models import Cadastro
from django.utils import timezone
from django.db.models import Count

from django.core.mail import send_mail

def cadastro_list(request):
    cadastrados = Cadastro.objects.all().values('lojacompra').annotate(total=Count('lojacompra')).order_by('lojacompra') 
    listacadastro = Cadastro.objects.all().order_by('lojacompra') 
    return render(request, 'inscricao/index.html', {'cadastrados': cadastrados, 'listacadastro': listacadastro})
    

def cadastro_list_pessoas(request):
    cadastrados = Cadastro.objects.all().values('lojacompra').annotate(total=Count('lojacompra')).order_by('lojacompra') 
    listacadastro = Cadastro.objects.all().order_by('lojacompra') 
    return render(request, 'inscricao/cadastro_list.html', {'cadastrados': cadastrados, 'listacadastro': listacadastro})

def confirmacao_inscricao(request):
    return render(request, 'inscricao/confirmacao.html')

def cadastro_detalhes(request):
    return render(request, 'inscricao/cadastro_list.html')

def cadastro_novo(request):
     if request.method == "POST":
         form = CadastroForm(request.POST)
         if form.is_valid():
             form.save()


             destinatario = form.data['email']
             nomedetinatario = form.data['nome']
             #print(str(destinatario) + ', se cadastrou para o pedala')
             send_mail('3º Pedala Centerbox',
             'Olá, ' + str(nomedetinatario) + '.' +
             '\n\nVocê acaba de se cadastrar no evento Pedala Centerbox, que acontecerá no dia 30/06/2019.' +
             '\nRetire seu kit entre os dias 27/06 a 29/06 na loja escolhida no ato da inscrição. ' +
             'Lembre-se de levar sua doação de leite para a retirada do kit e a impressão deste e-mail de confirmação.' +
             '\n\nAgora é só se preparar!'+
             '\n\n\n\nAtenciosamente,\nGrupo Centerbox.',
             'inscricao@pedalacenterbox.com.br',
             [str(destinatario)],
             fail_silently=False

             )

             cadastrados = Cadastro.objects.all().values('lojacompra').annotate(total=Count('lojacompra')).order_by('lojacompra') 
             listacadastro = Cadastro.objects.all().order_by('lojacompra') 
             return render(request, 'inscricao/confirmacao.html')

     else:
         form = CadastroForm()
     
     return render(request, 'inscricao/cadastro.html', {'form': form})

