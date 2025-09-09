from django import forms
from .models import Produto

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

        error_messages = {
            'nome':{'required':'O nome é um cmapo obrigatório',
                    'unique':'Produto já cadastrado'},
            'preco':{'required':'O preco do produto é um campo obrigatório'},
            'quantidade':{'required':'Quantidade de produtos é um campo obrigatório'},

        }