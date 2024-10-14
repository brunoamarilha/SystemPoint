from django.urls import path
from . import views

urlpatterns = [
    path('func/ponto', views.ver_ponto, name="ver_ponto"),
    path('func/menu', views.menu, name="menu")
]
