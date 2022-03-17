import re
from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    rg = models.CharField(max_length=11)
    cpf = models.CharField(max_length=9)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

class Curso(models.Model):
    NIVEL = (
        ("B", "Básico"),
        ("I", "Intermediário"),
        ("A", "Avançado"),
    )
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default="B") 
    
    def __str__(self):
        return self.descricao   
    