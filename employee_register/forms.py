from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname', 'emp_code', 'mobile', 'position')
        labels = {
            'fullname': 'Nome Completo',
            'emp_code': 'EMP. Code',
            'mobile': 'Telefone',
            'position': 'Ocupação'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Escolha"
        self.fields['emp_code'].required = False
