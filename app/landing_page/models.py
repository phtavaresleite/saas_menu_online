from django.db import models

# Create your models here.
class produto(models.Model):
    nome = models.CharField("Nome", max_length=50, blank=False, null=False)
    descricao = models.CharField("Descriçao", max_length=50, blank=False, null=False)
    categoria = models.CharField('Categoria', max_length=50, blank=False, null=False, default='Sanduiches')
    preco = models.DecimalField("Preço", max_digits=10, decimal_places=2, blank=False, null=False)
    imagem = models.ImageField("Foto",upload_to='produtos/', blank=False, null=False, default='app/media/produtos/placeholder.png')

    def __str__(self):
        return self.nome