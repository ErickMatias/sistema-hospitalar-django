from django import forms

from .models import Prontuario


class ProntuarioForm(forms.ModelForm):

    class Meta:

        model = Prontuario

        fields = [
            'consulta',
            'sintomas',
            'diagnostico',
            'prescricao',
            'observacoes'
        ]

        labels = {
            'consulta': 'Consulta',
            'sintomas': 'Sintomas',
            'diagnostico': 'Diagnóstico',
            'prescricao': 'Prescrição',
            'observacoes': 'Observações'
        }

        widgets = {
            'consulta': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'sintomas': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Descreva os sintomas do paciente'
                }
            ),

            'diagnostico': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Digite o diagnóstico'
                }
            ),

            'prescricao': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Digite a prescrição médica'
                }
            ),

            'observacoes': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'placeholder': 'Observações adicionais'
                }
            ),
        }

    def clean(self):

        cleaned_data = super().clean()

        consulta = cleaned_data.get('consulta')

        if not consulta:

            raise forms.ValidationError(
                'Selecione uma consulta.'
            )

        return cleaned_data