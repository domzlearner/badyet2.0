from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Savings
from .forms import SavingsForm, SavingUpdateForm

@login_required
def add_savings(request):
    if request.method == 'POST':
        form = SavingsForm(request.POST)
        if form.is_valid():
            savings = form.save(commit=False)
            savings.user = request.user
            print(f"Savings data: {savings}")
            savings.save()
            return redirect('dashboard')
        else:
            print(form.errors)
    else:
        form = SavingsForm()
    return render(request, 'savings/add_savings.html', {'form': form})

@login_required
def delete_savings(request, savings_id):
    savings = get_object_or_404(Savings, id=savings_id, user=request.user)
    
    if request.method == 'POST':
        savings.delete()
        return redirect('dashboard')

    return redirect('dashboard')

@login_required
def update_savings(request, savings_id):
    savings = get_object_or_404(Savings, id=savings_id, user=request.user)
    
    if request.method == 'POST':
        form = SavingUpdateForm(request.POST, instance=savings)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = SavingUpdateForm(instance=savings)
    
    return render(request, 'savings/update_savings.html', {'form': form, 'savings': savings})