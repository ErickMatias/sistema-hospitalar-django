from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from pacientes.models import Paciente
from consultas.models import Consulta
from prontuarios.models import Prontuario
from funcionarios.models import Funcionario


class DashboardView(LoginRequiredMixin, TemplateView):

    template_name = 'core/dashboard.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['total_pacientes'] = Paciente.objects.count()

        context['total_consultas'] = Consulta.objects.count()

        context['consultas_agendadas'] = Consulta.objects.filter(
            status='AGENDADA'
        ).count()

        context['total_prontuarios'] = Prontuario.objects.count()

        context['medicos_ativos'] = Funcionario.objects.filter(
            cargo='MEDICO',
            ativo=True
        ).count()

        return context