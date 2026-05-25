@"
# Sistema Hospitalar Django

Sistema hospitalar desenvolvido com Django, com autenticação de usuários, cadastro de pacientes, funcionários, consultas e prontuários.

## Funcionalidades

- Login e logout
- Dashboard inicial
- Cadastro de pacientes
- Cadastro de funcionários
- Agendamento de consultas
- Controle de status da consulta
- Cadastro de prontuários
- Controle de acesso por cargo
- Médico visualiza apenas suas consultas
- Recepcionista agenda consultas
- Admin possui acesso completo

## Tecnologias

- Python
- Django
- SQLite
- Bootstrap
- HTML/CSS

## Como rodar o projeto

```bash
git clone https://github.com/ErickMatias/sistema-hospitalar-django.git
cd sistema-hospitalar-django
python -m venv venv
venv\Scripts\activate
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
 