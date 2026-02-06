from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from utils.validador import validar_cpf
import re
# Create your models here.

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    idade = models.PositiveIntegerField
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=255)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=50)
    cep = models.CharField(max_length=12)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2, choices=[
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ])

    def __str__(self):
        return f'{self.usuario.first_name} {self.usuario.last_name}'
    
    def clean(self):
        error_messages = {}
        if not validar_cpf(self.cpf):
            error_messages['cpf'] = 'Digite um CPF válido.'
        if re.search(r'[^0-9]',self.cep) or len(self.cep) < 8:
            error_messages['cep'] = 'O CEP deve conter apenas números.'
        if error_messages:
            raise ValidationError(error_messages)
        
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'