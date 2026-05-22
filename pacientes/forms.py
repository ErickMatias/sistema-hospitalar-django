from django import forms
from .models import Paciente
from datetime import date


class PacienteForm(forms.ModelForm):

    class Meta:

        model = Paciente

        fields = [
            'nome',
            'cpf',
            'telefone',
            'data_nascimento'
        ]

        widgets = {

            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite o nome'
                }
            ),

            'cpf': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite o CPF'
                }
            ),

            'telefone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite o telefone'
                }
            ),

            'data_nascimento': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),

        }
    def clean_nome(self):
        nome = self.cleaned_data.get('nome')

        if len(nome) < 3:
            raise forms.ValidationError(
                'O nome deve possuir ao menos 3 caracteres.'
            )
        return nome
    
    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')

        if len(telefone) < 8:
            raise forms.ValidationError(
                'Telefone inválido'
            )
        
        return telefone
        
    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')

        paciente = Paciente.objects.filter(cpf = cpf).first().exclude(pk=self.instance.pk).first()

        if paciente:
            raise forms.ValidationError(
                'Já existe um paciente com esse cpf'
            )
        
        return cpf
    
    def clean(self):
        cleaned_data = super().clean()

        data_nascimento = cleaned_data.get(
            'data_nascimento'
        )

        if data_nascimento:
            hoje = date.today()

            if data_nascimento > hoje:
                raise forms.ValidationError(
                    ' A data de nascimento não pode ser uma futura.'
                )
            
            idade = hoje.year - data_nascimento.year

            if idade < 18:
                raise forms.ValidationError(
                    'O paciente deve ser maior de idade.'
                )
        return cleaned_data