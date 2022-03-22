from __future__ import annotations

from escola.models import Aluno
from escola.models import Curso
from rest_framework import serializers


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'sobrenome', 'rg', 'cpf', 'data_nascimento']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
