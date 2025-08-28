from django.views.generic import ListView
from .models import Fornecedores

class FornecedoresView(ListView):
    model = Fornecedores
    template_name = 'fornecedores.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(FornecedoresView, self).get_queryset()
        if buscar:
            return qs.filter(nome__icontains=buscar)
        return qs