from .models import Income
from django import forms

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['name', 'budget_amount', 'actual_amount', 'start_date', 'end_date']

class IncomeUpdateForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['actual_amount']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(initial=self.instance.name, disabled=True)