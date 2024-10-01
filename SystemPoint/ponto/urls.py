from django.urls import path
from . import views

urlpatterns = [
    path('func/', views.ver_ponto, name="ver_ponto"),
    path('func/inserir', views.inserir_ponto, name="inserir_ponto")
]
