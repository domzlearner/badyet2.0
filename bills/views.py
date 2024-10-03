from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Bills
from .forms import BillsForm, BillsUpdateForm

@login_required
def add_bills(request):
    if request.method == 'POST':
        form = BillsForm(request.POST)
        if form.is_valid():
            bills = form.save(commit=False)
            bills.user = request.user
            print(f"Bills data: {bills}")
            bills.save()
            return redirect('dashboard')
        else:
            print(form.errors)
    else:
        form = BillsForm()
    return render(request, 'bills/add_bills.html', {'form': form})

@login_required
def delete_bills(request, bills_id):
    bills = get_object_or_404(Bills, id=bills_id, user=request.user)
    
    if request.method == 'POST':
        bills.delete()
        return redirect('dashboard')

    return redirect('dashboard')

@login_required
def update_bills(request, bills_id):
    bills = get_object_or_404(Bills, id=bills_id, user=request.user)
    
    if request.method == 'POST':
        form = BillsUpdateForm(request.POST, instance=bills)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BillsUpdateForm(instance=bills)
    
    return render(request, 'bills/update_bills.html', {'form': form, 'bills': bills})