from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('employeeList/', views.EmployeesListView.as_view(), name='employee-list'),
    path('employee/<int:pk>', views.EmployeeDetailView.as_view(), name='employee-detail'),
]