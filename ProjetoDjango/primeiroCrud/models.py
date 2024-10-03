from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=100) #nome do produto com o maximo de 100 caracteres

    descricao = models.TextField() #descricao do produto com textos longos

    preco = models.DecimalField(max_digits=8, decimal_places=2) #preco do produto de ate 8 digitos e duas casas decimais

    def __str__(self):
       return self.nome #retorna o nome do do profuto quando o objeto é convertido para string
        
        