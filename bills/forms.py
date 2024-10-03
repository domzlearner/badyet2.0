from .models import Bills
from django import forms

class BillsForm(forms.ModelForm):
    class Meta:
        model = Bills
        fields = ['name', 'budget_amount', 'actual_amount', 'due_date']

class BillsUpdateForm(forms.ModelForm):
    class Meta:
        model = Bills
        fields = ['actual_amount', 'due_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(initial=self.instance.name, disabled=True)