from agendamentos.models import Agendamento
from django.contrib import admin

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('horario', 'cliente', 'funcionario', 'valor')
    search_fields = ('cliente', 'funcionario')
    list_filter = ('cliente', 'servico')
