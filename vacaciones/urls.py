#Se creo ya que no exisatia

from django.urls import path
from . import views

app_name = 'vacaciones'

urlpatterns = [
    path('empleados/',                      views.EmpleadoListView.as_view(),   name='empleado_list'),
    path('empleados/nuevo/',                views.EmpleadoCreateView.as_view(), name='empleado_create'),
    path('empleados/<int:pk>/editar/',      views.EmpleadoUpdateView.as_view(), name='empleado_update'),
    path('empleados/<int:pk>/eliminar/',    views.EmpleadoDeleteView.as_view(), name='empleado_delete'),
]
