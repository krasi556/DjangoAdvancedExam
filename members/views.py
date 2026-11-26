from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from rest_framework.permissions import IsAuthenticated
from django.urls import reverse_lazy
from rest_framework.viewsets import ModelViewSet

from employees.models import Employee
from members.forms import EndorsementForm
from members.models import Endorsement
from members.permissions import EmployeeTierAccess
from members.serializers import EmployeeWriteSerialize, CasualEmployee


# Create your views here.


class EmployeeViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, EmployeeTierAccess]
    queryset = Employee.objects.all()
    serializer_class = EmployeeWriteSerialize  # THIS WILL BE CHANGED  WITH EmployeeWriteSerialize IF I GOT TIME LEFT !!!!!!


class EndorsementDonateView(CreateView):
    success_url = reverse_lazy('accounts:profile')
    model = Endorsement
    form_class = EndorsementForm
    template_name = 'employees/focused-employee.html'

    def get_employee(self):
        return get_object_or_404(Employee, id=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee'] = self.get_employee()
        return context

    def form_valid(self, form):
        form.instance.sponsor = self.request.user
        form.instance.employee = self.get_employee()
        return super().form_valid(form)
