from django.db.models import Q, Sum
from income.models import Income
from savings.models import Savings
from bills.models import Bills
from django.contrib.auth.decorators import login_required

@login_required
def budget_donut_chart(request):
    user = request.user

    incomes = Income.objects.filter(user=user)

    total_budget_income = 0
    total_actual_income = 0

    total_budget_income = incomes.aggregate(total_budget=Sum('budget_amount'))['total_budget'] or 0
    total_actual_income = incomes.aggregate(total_actual=Sum('actual_amount'))['total_actual'] or 0


    income_start_date = incomes.earliest('start_date').start_date if incomes.exists() else None
    income_end_date = incomes.latest('end_date').end_date if incomes.exists() else None

    if income_start_date and income_end_date:
        total_budget_savings = Savings.objects.filter(
            user=user,
            start_date__gte=income_start_date,
            end_date__lte=income_end_date
        ).aggregate(total_budget_savings=Sum('budget_amount'))['total_budget_savings'] or 0

        total_actual_savings = Savings.objects.filter(
            user=user,
            start_date__gte=income_start_date,
            end_date__lte=income_end_date
        ).aggregate(total_actual_savings=Sum('actual_amount'))['total_actual_savings'] or 0

        total_budget_bills = Bills.objects.filter(
            user=user,
            due_date__gte=income_start_date,
            due_date__lte=income_end_date
        ).aggregate(total_budget_bills=Sum('budget_amount'))['total_budget_bills'] or 0

        total_actual_bills = Bills.objects.filter(
            user=user,
            due_date__gte=income_start_date,
            due_date__lte=income_end_date
        ).aggregate(total_actual_bills=Sum('actual_amount'))['total_actual_bills'] or 0

    else:
        total_budget_savings = total_actual_savings = total_budget_bills = total_actual_bills = 0

    remaining_budget = total_budget_income - total_budget_savings - total_budget_bills
    remaining_actual = total_actual_income - total_actual_savings - total_actual_bills

    context = {
        'total_budget_income': total_budget_income,
        'total_budget_savings': total_budget_savings,
        'total_budget_bills': total_budget_bills,
        'remaining_budget': remaining_budget,
        'total_actual_income': total_actual_income,
        'total_actual_savings': total_actual_savings,
        'total_actual_bills': total_actual_bills,
        'remaining_actual': remaining_actual,
    }
    
    return context
