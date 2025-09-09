from django.urls import path

from .views import ServicosView, ServicoAddView, ServicoUpdateView, ServicoDeleteView, ServicoInLineEditView

urlpatterns = [
    path('servicos', ServicosView.as_view(), name='servicos'),
    path('servicos/adicionar', ServicoAddView.as_view(), name='servico_adicionar'),
    path('<int:pk>servicos/editar', ServicoUpdateView.as_view(), name='servico_editar'),
    path('<int:pk>servicos/apagar', ServicoDeleteView.as_view(), name='servico_apagar'),
    path('<int:pk>servicos/inline', ServicoInLineEditView.as_view(), name='servico_inline'),

]