from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Empleado

class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'vacaciones/empleado_list.html'
    context_object_name = 'empleados'

class EmpleadoCreateView(CreateView):
    model = Empleado
    fields = ['nombre', 'email', 'fecha_ingreso', 'dias_disponibles']
    template_name = 'vacaciones/empleado_form.html'
    success_url = reverse_lazy('vacaciones:empleado_list')

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    fields = ['nombre', 'email', 'fecha_ingreso', 'dias_disponibles']
    template_name = 'vacaciones/empleado_form.html'
    success_url = reverse_lazy('vacaciones:empleado_list')

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'vacaciones/empleado_confirm_delete.html'
    success_url = reverse_lazy('vacaciones:empleado_list')
