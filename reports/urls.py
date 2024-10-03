from django.urls import path
from . import views

urlpatterns = [
    path('budget-donut-chart/', views.budget_donut_chart, name='budget_donut_chart'),
]