from django import forms

from .models import Cliente


class ClienteModelForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'endereco', 'fone', 'email', 'foto']

        error_messages = {
            'nome': {'required':'O nome do cliente é um campo obrigatório'},
            'endereco': {'required':'O endereço do cliente é um campo obrigatório'},
            'fone': {'required':'O telefone do cliente é um campo obrigatório'},
            'email': {'required':'O email do cliente é um campo obrigatorio',
                      'invalid':'Formato invalido para email. Ex: de formato valido: fulano@dominio.com',
                      'unique':'E-mail ja cadastrado'
                      }

        }