from django import forms
from .models import Cadastro, Empresa

class CadastroForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(
        attrs ={
            'class': 'input1',
            'placeholder': 'Nome',
            'maxlength': '200',
            'required': ''
        }
    ))

    email = forms.EmailField(widget=forms.TextInput(
        attrs ={
            'class': 'input1',
            'placeholder': 'E-mail',
            'required': ''
        }
    ))

    telefone = forms.CharField(widget=forms.TextInput(
        attrs ={
            'class': 'input1',
            'placeholder': 'Telefone',
            'maxlength': '20',
            'type': 'number',
        }
    ))
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
    """
    LOJA_CHOICES = [
        [1, "01-GENIBAU"],
        [2, "02-PARQUE SÃO JOSE"],
        [3, "03-JOÃO XXIII"],
        [4, "04-JARDIM IRACEMA"],
        [5, "05-SANTOS DUMONT"],
        [6, "06-MESSEJANA"],
        [7, "07-PARQUELANDIA"],
        [8, "08-JOSE BASTOS"],
        [9, "09-CONCEITO"],
        [10, "10-BARRA DO CEARA"],
        [11, "11-EXPEDICIONARIOS"],
        [12, "12-WASHINGTON SOARES"],
        [13, "13-CAUCAIA"],
        [14, "14-BARRA DO CEARA II"],
    ]
    """
    lojacompra = forms.IntegerField(widget=forms.Select(
        choices=LOJA_CHOICES,
        attrs ={
            'class': 'input1',
            'placeholder': 'Loja de retirada do kit'
        }
    ))

    dtnascimento = forms.DateField(widget=forms.DateInput(
        attrs ={
            'class': 'input1',
            'type': 'date',
            'placeholder': 'Data de nascimento'
        }
    ))

    ALUGAR_CHOICES = [
        ['S', 'sim, vou alugar.'],
        ['N', 'não, já tenho minha bike.'],
    ]

    alugar = forms.CharField(widget=forms.RadioSelect(
        choices=ALUGAR_CHOICES
    ))

    SN_CHOICES = [
        ['S', 'Sim'],
        ['N', 'Não'],
    ]
    outeventos = forms.CharField(widget=forms.RadioSelect(
        choices=SN_CHOICES
    ))

    class Meta:
        model = Cadastro
        fields = ["nome", "email", "telefone", "lojacompra", "outeventos", "alugar"]

        """
        fields = ["nome", "email", "telefone", "lojacompra", "sexo"
        , "outeventos", "alugar"]
        """

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ["seqempresa", "nomeempresa"]