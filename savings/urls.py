from django.urls import path
from . import views

urlpatterns = [
    path('add_savings/', views.add_savings, name='add_savings'),
    path('delete_savings/<int:savings_id>/', views.delete_savings, name='delete_savings'),
    path('update_savings/<int:savings_id>/', views.update_savings, name='update_savings'),
]