from django.urls import path
from . import views

urlpatterns = [
    path('add_bills/', views.add_bills, name='add_bills'),
    path('delete_bills/<int:bills_id>/', views.delete_bills, name='delete_bills'),
    path('update_bills/<int:bills_id>/', views.update_bills, name='update_bills'),
]