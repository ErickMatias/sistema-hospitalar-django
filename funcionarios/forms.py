from django import forms
from .models import Funcionario


class FuncionarioForm(forms.ModelForm):

    class Meta:

        model = Funcionario

        fields = [
            'nome',
            'cpf',
            'cargo',
            'especialidade',
            'ativo'
        ]

        labels = {

            'nome': 'Nome Completo',
            'cpf': 'CPF',
            'cargo': 'Cargo',
            'especialidade': 'Especialidade',
            'ativo': 'Ativo'

        }

        help_texts = {

            'cpf': 'Digite apenas números'

        }

        widgets = {

            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite o nome do funcionário'
                }
            ),

            'cpf': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite o CPF'
                }
            ),

            'cargo': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'especialidade': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite a especialidade'
                }
            ),

            'ativo': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),

        }

    def clean_cpf(self):

        cpf = self.cleaned_data['cpf']

        funcionario = Funcionario.objects.filter(
            cpf=cpf
        )

        if self.instance.pk:

            funcionario = funcionario.exclude(
                pk=self.instance.pk
            )

        if funcionario.exists():

            raise forms.ValidationError(
                'Já existe um funcionário com esse CPF.'
            )

        return cpf