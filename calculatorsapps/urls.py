from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('calculator_list')),  # Redirect /calculators/ to /calculators/list/
    path('list/', views.calculator_list, name='calculator_list'),
]