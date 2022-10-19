from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
import hashlib
from .models import Employee

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class EmployeesListView(generic.ListView):
    model = Employee
    # template_name = '/accounts/employee_list.html'

class EmployeeDetailView(generic.DetailView):
    model = Employee
    # template_name = '/accounts/employee_detail.html'