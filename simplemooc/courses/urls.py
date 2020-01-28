from django.urls import path, include

# O include permite ir aos URL'S dos aplicativos e não ficar uma bagunça os endereços.

from . import views

urlpatterns = [
    path('', views.Cursos),
    #path('<int:pk>', views.details), #Esta é a forma de passar um parametro pelo navegador.
    path('<slug:slug>', views.details),
]
