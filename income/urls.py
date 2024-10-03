from django.urls import path
from . import views

urlpatterns = [
    path('add_income/', views.add_income, name='add_income'),
    path('delete_income/<int:income_id>/', views.delete_income, name='delete_income'),
    path('update_actual_amount/<int:income_id>/', views.update_actual_amount, name='update_actual_amount'),
]