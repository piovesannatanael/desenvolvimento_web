from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField('Nome', max_length=70, help_text='Nome do fornecedor')
    cnpj = models.CharField('CNPJ', max_length=18, help_text='CNPJ do fornecedor')
    fone = models.CharField('Fone', max_length=20, help_text='Fone do fornecedor')


    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.nome