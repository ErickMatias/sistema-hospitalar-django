from django.db import models
from django.contrib.auth.models import User


class Funcionario(models.Model):

    CARGOS = [
        ('MEDICO', 'Médico'),
        ('RECEPCIONISTA', 'Recepcionista'),
        ('ADMIN', 'Administrador')
    ]

    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='funcionario'
    )

    nome = models.CharField(max_length=255)

    cpf = models.CharField(
        max_length=14,
        unique=True
    )

    cargo = models.CharField(
        max_length=20,
        choices=CARGOS
    )

    especialidade = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    ativo = models.BooleanField(default=True)

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.nome} - {self.cargo}'