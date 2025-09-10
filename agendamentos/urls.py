from django.urls import path

from agendamentos.views import AgendamentosView, AgendamentoAddView, AgendamentoUpdateView, AgendamentoDeleteView, \
    AgendamentoInLineEditView

urlpatterns = [
    path('agendamentos', AgendamentosView.as_view(), name='agendamentos'),
    path('agendamentos/adicionar', AgendamentoAddView.as_view(), name='agendamento_adicionar'),
    path('<int:pk>agendamentos/editar', AgendamentoUpdateView.as_view(), name='agendamento_editar'),
    path('<int:pk>agendamentos/apagar', AgendamentoDeleteView.as_view(), name='agendamento_apagar'),
    path('<int:pk>agendamentos/inline', AgendamentoInLineEditView.as_view(), name='agendamento_inline'),
]