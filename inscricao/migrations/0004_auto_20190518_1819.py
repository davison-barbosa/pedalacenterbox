# Generated by Django 2.2.1 on 2019-05-18 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscricao', '0003_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='lojacompra',
            field=models.CharField(choices=[[1, '01-GENIBAU'], [2, '02-PARQUE SÃO JOSE'], [3, '03-JOÃO XXIII'], [4, '04-JARDIM IRACIMA'], [5, '05-SANTOS DUMONT'], [6, '06-MESSEJANA'], [7, '07-PARQUELANDIA'], [8, '08-JOSE BASTOS'], [9, '09-CONCEITO'], [10, '10-BARRA DO CEARA'], [11, '11-EXPEDICIONARIOS'], [12, '12-WASHINGTON SOARES'], [13, '13-CAUCAIA'], [14, '14-BARRA DO CEARA II']], max_length=5),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='telefone',
            field=models.CharField(max_length=20),
        ),
    ]
