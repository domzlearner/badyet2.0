from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Income
from .forms import IncomeForm, IncomeUpdateForm

@login_required
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            print(f"Income data: {income}")
            income.save()
            return redirect('dashboard')
        else:
            print(form.errors)
    else:
        form = IncomeForm()
    return render(request, 'income/add_income.html', {'form': form})

@login_required
def delete_income(request, income_id):
    income = get_object_or_404(Income, id=income_id, user=request.user)
    
    if request.method == 'POST':
        income.delete()
        return redirect('dashboard')

    return redirect('dashboard')


@login_required
def update_actual_amount(request, income_id):
    income = get_object_or_404(Income, id=income_id, user=request.user)
    
    if request.method == 'POST':
        form = IncomeUpdateForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = IncomeUpdateForm(instance=income)
    
    return render(request, 'income/update_income.html', {'form': form, 'income': income})