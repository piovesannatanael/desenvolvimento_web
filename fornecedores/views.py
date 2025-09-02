from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Fornecedores
from .forms import FornecedoresModelForm

class FornecedoresView(ListView):
    model = Fornecedor
    template_name = 'fornecedores.html'


    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(FornecedoresView, self).get_queryset()
        if buscar:
            return qs.filter(nome__icontains=buscar)
        return qs

class FornecedorAddView(CreateView):
    model = Fornecedor
    form_class = FornecedorModelForm
    template_name = 'fornecedor_form.html'
    success_url = reverse_lazy('fornecedores')