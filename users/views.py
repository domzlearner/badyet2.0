from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, UserRegistrationForm
from income.models import Income
from savings.models import Savings
from reports.views import budget_donut_chart

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            profile = profile_form.save(commit=False)
            profile.user = new_user
            profile.save()
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
        profile_form = UserProfileForm() 
    return render(request, 'users/register.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def dashboard_view(request):
    user=request.user
    incomes = Income.objects.filter(user=request.user)
    savings = Savings.objects.filter(user=request.user)
    # print(f"Income data | user: {incomes} | {user}")

    chart_data = budget_donut_chart(request)
    # print("Chart data:", chart_data)

    return render(request, 'users/dashboard.html', {
        'user': user,
        'incomes': incomes,
        'savings': savings,
        'total_budget_income': chart_data['total_budget_income'],
        'total_budget_savings': chart_data['total_budget_savings'],
        'remaining_budget': chart_data['remaining_budget'],
        'total_actual_income': chart_data['total_actual_income'],
        'total_actual_savings': chart_data['total_actual_savings'],
        'remaining_actual': chart_data['remaining_actual'],
    })