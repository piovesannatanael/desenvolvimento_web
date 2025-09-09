from django.urls import path

from agendamentos.views import AgendamentosView, AgendamentoAddView, AgendamentoUpdateView, AgendamentoDeleteView

urlpatterns = [
    path('agendamentos', AgendamentosView.as_view(), name='agendamentos'),
    path('agendamentos/adicionar', AgendamentoAddView.as_view(), name='agendamento_adicionar'),
    path('<int:pk>agendamentos/editar', AgendamentoUpdateView.as_view(), name='agendamento_editar'),
    path('<int:pk>agendamentos/apagar', AgendamentoDeleteView.as_view(), name='agendamento_apagar'),
]