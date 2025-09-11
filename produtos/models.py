from django.db import models
from django.db.models.functions import Upper

import fornecedores.models

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=50, help_text='Nome da produto', unique=True)
    preco = models.DecimalField('Preço', max_digits=5, decimal_places=2, help_text='Preço do produto')
    quantidade = models.DecimalField('Quantidade', max_digits=5, decimal_places=2, help_text='Quantidade de produtos em estoque')
    fornecedor = models.ForeignKey(fornecedores.models.Fornecedor, verbose_name='Fornecedor', help_text='Nome do fornecedor',
                                   on_delete=models.PROTECT, related_name='fornecedor')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = [Upper('nome')]


    def __str__(self):
        return self.nome