from django.urls import path
from aplicacaoAppadaria.views import index, pedido, fila
 
urlpatterns = [
    path('', index, name='index'),
    path('pedido/', pedido, name='pedido'),
    path('fila/', fila, name='fila'),
]



