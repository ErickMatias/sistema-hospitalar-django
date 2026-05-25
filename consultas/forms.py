from django import forms
from django.utils import timezone
from .models import Consulta


class ConsultaForm(forms.ModelForm):

    class Meta:

        model = Consulta

        fields = [
            'paciente',
            'medico',
            'data_consulta',
            'observacoes'
        ]

        widgets = {

            'paciente': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'medico': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'data_consulta': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'datetime-local'
                }
            ),

            'observacoes': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4
                }
            ),
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['medico'].queryset = self.fields['medico'].queryset.filter(
            cargo='MEDICO',
            ativo=True
        )

    def clean_data_consulta(self):

        data_consulta = self.cleaned_data.get(
            'data_consulta'
        )

        if data_consulta < timezone.now():

            raise forms.ValidationError(
                'A consulta não pode ser marcada no passado.'
            )

        return data_consulta

    def clean(self):

        cleaned_data = super().clean()

        medico = cleaned_data.get('medico')

        data_consulta = cleaned_data.get('data_consulta')

        if medico and data_consulta:

            consulta_existente = Consulta.objects.filter(
                medico=medico,
                data_consulta=data_consulta,
                status='AGENDADA'
            )

            if self.instance.pk:

                consulta_existente = consulta_existente.exclude(
                    pk=self.instance.pk
                )

            if consulta_existente.exists():

                raise forms.ValidationError(
                    'Este médico já possui consulta nesse horário.'
                )

        return cleaned_data
    
    def clean_consulta(self):

        consulta = self.cleaned_data.get('consulta')

        if consulta.status == 'CANCELADA':

            raise forms.ValidationError(
                'Não é possível criar prontuário para uma consulta cancelada.'
            )

        return consulta