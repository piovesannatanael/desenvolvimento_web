from django.urls import path
from .views import ProdutosView, ProdutoAddView, ProdutoUpdateView, ProdutoDeleteView

urlpatterns = [
    path('produtos', ProdutosView.as_view(), name='produtos'),
    path('produtos/adicionar',ProdutoAddView.as_view(), name='produto_adicionar'),
    path('<int:pk>produtos/editar',ProdutoUpdateView.as_view(), name='produto_editar'),
    path('<int:pk>produtos/apagar',ProdutoDeleteView.as_view(), name='produto_apagar'),
]