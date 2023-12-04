from django.urls import path
from . import views
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('icons/favicon.ico'))), 
    path('', views.home, name="home"),
    path('executar', views.executar, name='executar'),
    path('passo', views.PassoAPasso, name='PassoAPasso'),
    path('criarSwap/<str:vetor_qtd_pro>/<str:vetor_tam_pro>/', views.criarSwap, name='criarSwap'),
    path('criarListaProcessos/<int:aleatorio>/<int:lote>/<int:qtdProExe>/<str:listaProcessos>', views.criarListaProcessos, name='CriarListaProcessos'),
    path('criarMemorias/<str:vetorX>/<int:Y>/<int:pageSize>/<int:swapAle>', views.criarMemorias, name='criarMemorias'),
    path('resultado', views.Resultados, name="Resultados"),
]
