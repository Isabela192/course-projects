from __future__ import annotations

from escola.models import Aluno
from escola.models import Curso
from rest_framework import viewsets

from .serializer import AlunoSerializer
from .serializer import CursoSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos do banco

    """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """
    Exibindo os cursos
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
