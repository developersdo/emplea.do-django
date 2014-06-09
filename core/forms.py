# Formularios
from django import forms
from models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Programador Web/DBA/Python Hacker"}),
            "place": forms.TextInput(attrs={"placeholder": "Santo Domingo/Santiago/Remoto"}),
            "company_name": forms.TextInput(attrs={"placeholder": "Mi Empresa, SRL"}),
            "url": forms.TextInput(attrs={"placeholder": "http://miempresa.com"}),
            "email": forms.TextInput(attrs={"placeholder": "info@miempresa.com"}),

        }
