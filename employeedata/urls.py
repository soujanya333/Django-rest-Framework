from django.urls import path
from .views import EmployeeList, UpdateEmployee

urlpatterns = [
    path('getall',EmployeeList.as_view()),
    path('updateemployee',UpdateEmployee.as_view())
]