from django.db import models
from django.contrib.auth.models import User

class Income(models.Model):
    name = models.CharField(max_length=100, default='Payslip')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    budget_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    actual_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name