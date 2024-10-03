from .models import Savings
from django import forms

class SavingsForm(forms.ModelForm):
    class Meta:
        model = Savings
        fields = ['name', 'budget_amount', 'actual_amount', 'start_date', 'end_date']

class SavingUpdateForm(forms.ModelForm):
    class Meta:
        model = Savings
        fields = ['actual_amount']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(initial=self.instance.name, disabled=True)