from django.db import models
from django.utils import timezone
#from phone_field import PhoneField

# Create your models here.


class Cadastro(models.Model):
    SEXO_CHOICES = [
        ["F", "Feminino"],
        ["M", "Masculino"],
        ["N", "Nenhuma das opções"]
    ]

    OPCAO = [
        ["S", "Sim"],
        ["N", "Não"]
    ]

    LOJA_CHOICES = [
        [1, "Centerbox Genibau"],
        [2, "Centerbox Parque São José"],
        [6, "Centerbox Messejana"],
        [8, "Centerbox José Bastos"],
        [9, "Centerbox Conceito"],
        [10, "Centerbox Barra do Ceará"],
        [11, "Centerbox Expedicionarios"],
        [12, "Centerbox Washington Soares"],
    ]

    nome = models.CharField(max_length=200, null=False)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, null=False)
    #telefone = PhoneField(blank=True, help_text='Contact phone number')
    lojacompra = models.IntegerField(choices=LOJA_CHOICES)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    outeventos = models.CharField(max_length=1, choices=OPCAO)
    alugar = models.CharField(max_length=1, choices=OPCAO)
    criado_em = models.DateTimeField('criado em', auto_now_add=True) 


    def publish(self):
            self.save()

class Empresa(models.Model):
    seqempresa = models.IntegerField(unique=True)
    nomeempresa = models.CharField(max_length=200, null=False)
"""
class Usuario(models.Model):
    SEXO_CHOICES = [
        ["F", "Feminino"],
        ["M", "Masculino"],
        ["N", "Nenhuma das opções"]
    ]

    nome = models.CharField(max_length=20, null=False)
    email = models.EmailField(null=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
"""
