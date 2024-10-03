from django.db import models
from django.contrib.auth.models import User

class Bills(models.Model):
    name = models.CharField(max_length=100, default='Meralco')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    budget_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    actual_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name