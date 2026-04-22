from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('trayectoria/', views.trayectoria, name='trayectoria'),
    path('contacto/', views.contacto, name='contacto'),
]
