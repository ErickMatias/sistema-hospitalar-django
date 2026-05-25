from django.db import models
from consultas.models import Consulta

class Prontuario(models.Model):
    consulta = models.OneToOneField(
        Consulta,
          on_delete=models.CASCADE
          )
    
    sintomas = models.TextField()
    diagnostico = models.TextField()
    prescricao = models.TextField()

    observacoes = models.TextField(
        blank=True,
        null=True
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'Prontuário - {self.consulta.paciente}'

