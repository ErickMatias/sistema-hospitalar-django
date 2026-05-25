from django.db import models
from pacientes.models import Paciente
from funcionarios.models import Funcionario
from django.contrib.auth.models import User


class Consulta(models.Model):

    STATUS_CHOICES = [
        ('AGENDADA', 'Agendada'),
        ('REALIZADA', 'Realizada'),
        ('CANCELADA', 'Cancelada'),
    ]

    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE
    )

    medico = models.ForeignKey(
        Funcionario,
        on_delete=models.CASCADE,
        related_name='consultas_medico',
        limit_choices_to={'cargo': 'MEDICO'}
    )

    data_consulta = models.DateTimeField()

    observacoes = models.TextField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='AGENDADA'
    )

    criado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.paciente} - {self.data_consulta}'