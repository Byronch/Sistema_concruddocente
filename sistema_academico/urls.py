"""sistema_academico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from core import views

urlpatterns = [
    path('', views.home, name="home"),
    path('Asistencias/', views.asistencia, name="asistencia"),
    path('Notas/', views.notas, name="notas"),
    path('Personal/', views.personal, name="personal"),
    path('Estudiantes/', views.estudiantes, name="estudiantes"),
    path('Materias/', views.materias, name="materias"),
    path('Cursos/', views.materias, name="cursos"),
    path('login/', views.login, name="login"),
    path('Consultar/', views.Consultar, name="Consultar"),
    path('enero/', views.enero, name="enero"),
    path('febrero/', views.febrero, name="febrero"),
    path('marzo/', views.marzo, name="marzo"),
    path('abril/', views.abril, name="abril"),
    path('mayo/', views.mayo, name="mayo"),
    path('junio/', views.junio, name="junio"),
    path('julio/', views.julio, name="julio"),
    path('agosto/', views.agosto, name="agosto"),
    path('septiembre/', views.septiembre, name="septiembre"),
    path('octubre/', views.octubre, name="octubre"),
    path('noviembre/', views.noviembre, name="noviembre"),
    path('diciembre/', views.diciembre, name="diciembre"),
    path('admin/', admin.site.urls),
]
