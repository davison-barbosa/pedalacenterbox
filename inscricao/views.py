
#from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .forms import *
from .models import Cadastro
from django.utils import timezone
from django.db.models import Count
#from django.shortcuts import redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from email.mime.text import *
from django.template import loader

def cadastro_list(request):
    #cadastrados = Cadastro.objects.filter(lojacompra=lojacompra)
    #cadastrados = Cadastro.objects.values('lojacompra').annotate(dcount=Count('lojacompra'))
    #cadastrados = Cadastro.objects.values('lojacompra').count()
    cadastrados = Cadastro.objects.all().values('lojacompra').annotate(total=Count('lojacompra')).order_by('lojacompra') 
    listacadastro = Cadastro.objects.all().order_by('lojacompra') 
    #cadastrados = Cadastro.objects.order_by('criado_em')
    #return render(request, 'inscricao/index.html')
    return render(request, 'inscricao/index.html', {'cadastrados': cadastrados, 'listacadastro': listacadastro})
    #return render(request, 'inscricao/cadastro_list.html', {'cadastrados': cadastrados, 'listacadastro': listacadastro})


def cadastro_list_pessoas(request):
    #cadastrados = Cadastro.objects.filter(lojacompra=lojacompra)
    #cadastrados = Cadastro.objects.values('lojacompra').annotate(dcount=Count('lojacompra'))
    #cadastrados = Cadastro.objects.values('lojacompra').count()
    #cadastrados = Cadastro.objects.order_by('criado_em')
    #return render(request, 'inscricao/index.html')
    cadastrados = Cadastro.objects.all().values('lojacompra').annotate(total=Count('lojacompra')).order_by('lojacompra') 
    listacadastro = Cadastro.objects.all().order_by('lojacompra') 
    return render(request, 'inscricao/cadastro_list.html', {'cadastrados': cadastrados, 'listacadastro': listacadastro})
    #return render(request, 'inscricao/cadastro_list.html', {'cadastrados': cadastrados, 'listacadastro': listacadastro})

#def cadastro_novo(request):
#    form = CadastroForm()
#    return render(request, 'inscricao/cadastro_novo.html', {'form': form})

def confirmacao_inscricao(request):
    return render(request, 'inscricao/confirmacao.html')

def cadastro_detalhes(request):
    #post = get_object_or_404(Cadastro, pk=pk)
    #return render(request, 'inscricao/cadastro_detalhes.html', {'post': post})
    #cadastrados = Cadastro.objects.all().values('lojacompra').annotate(total=Count('lojacompra')).order_by('lojacompra') 
    #cadastrados = Cadastro.objects.order_by('criado_em')
    #return render(request, 'inscricao/cadastro_list.html', {'cadastrados': cadastrados})
    return render(request, 'inscricao/cadastro_list.html')

def cadastro_novo(request):
     if request.method == "POST":
         form = CadastroForm(request.POST)
         if form.is_valid():
             #post = form.save(commit=False)
             #post.save()
             form.save()
             

             #msg.attach(MIMEText('<html><body><p><img src="emailconfirmacao.jpg"></p></body></html>', 'html', 'utf-8'))
             #msg = MIMEText('<html><body><p><img src="emailconfirmacao.jpg"></p></body></html>', 'html', 'utf-8')
             #msg = '<html><body><img class="img-responsive" itemprop="logo" src="http://centerbox.com.br/wp-content/themes/oficial/img/marca.png" alt="Centerbox Supermercado em Fortaleza – encartes, ofertas do dia."></body></html>'
             #msgg = '<html><body><img class="img-responsive" itemprop="logo" src="/static/img/bg-callout2.jpg" alt="Centerbox Supermercado em Fortaleza – encartes, ofertas do dia."></body></html>'
             #msgdois = '{% load staticfiles %}<html><body><img src="{% static "img/bg-callout2.gif" %}"></body></html>'
             #'<img src="/static/img/bg-callout2.jpg">'

             destinatario = form.data['email']
             nomedetinatario = form.data['nome']
             print(str(destinatario) + ', se cadastrou para o pedala')
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
             #,html_message=msgg
             )

             cadastrados = Cadastro.objects.all().values('lojacompra').annotate(total=Count('lojacompra')).order_by('lojacompra') 
             listacadastro = Cadastro.objects.all().order_by('lojacompra') 
             #return render(request, 'inscricao/index.html', {'cadastrados': cadastrados, 'listacadastro': listacadastro})
             return render(request, 'inscricao/confirmacao.html')
             #return HttpResponseRedirect(reverse('inscricao/index.html'))
             #return redirect('cadastro_detalhes') #, pk=post.pk)
     else:
         form = CadastroForm()
     
     return render(request, 'inscricao/cadastro.html', {'form': form})

"""
def envio_email(request):
    send_mail('3 Pedala centerbox',
    'Você acacaba de se cadastrara no evento pedala centerbox, que acontecera no dia tal',
    'davison-barbosa@outlook.com',
    ['helena4682@yahoo.com'],
    fail_silently=False
    )
    return render(request, 'inscricao/cadastro_novo.html', {'form': form})
"""
#def cadastrar_usuario(request):
#    form = CadastroForm()
#    return render(request, "form.html", {'form':form})
