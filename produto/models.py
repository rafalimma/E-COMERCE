from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.CharField()
    imagem = models.ImageField(upload_to='images/%Y/%M', blank=True, null=True)
    slug = models.SlugField(unique=True)
    preco_marketing = models.FloatField(default=0)
    preco_marketing_promocional = models.FloatField(default=0)
    tipo = models.CharField(default='V', max_length=1, choices=(
        ('V', 'Variação'),
        ('S', 'Simples')
    ))

def resize_image(img, new_width=800):
    print(img.name)

def save(self, *args, **kwargs):
    super().save(*args, *kwargs)

    max_image_size = 800
    if self.imagem:
        self.resize_image(self.imagem, max_image_size)

def __str__(self):
    return self.nome