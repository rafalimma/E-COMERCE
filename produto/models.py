from django.db import models
from PIL import Image
import os
from django.conf import settings

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

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_w, original_h = img_pil.size

        if original_w <= new_width:
            img_pil.close()
            return
        
        new_h = round((new_width * original_h) / original_w)
        new_img = img_pil.resize((new_width, new_h), Image.LANCZOS)
        new_img.save(img_full_path, optimize=True, quality=50)

    def save(self, *args, **kwargs):
        super().save(*args, *kwargs)

        max_image_size = 800
        if self.imagem:
            self.resize_image(self.imagem, max_image_size)

    def __str__(self):
        return self.nome
    
class Variacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, blank=True, null=True)
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    estoque = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nome or self.produto.nome