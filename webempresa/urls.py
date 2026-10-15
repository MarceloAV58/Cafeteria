"""
URL configuration for webempresa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from services import views as services_views
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', blog_views.blog, name='blog'),
    path('blog/categoria/<str:category_name>/', blog_views.categorias, name='categorias'),
    path('sample/', views.sample, name='sample'),
    path('services/', services_views.services, name='services'),
    path('services/productos', services_views.lista_productos, name='services'),
    path('services/servicios', services_views.lista_servicios, name='services'),
    path('store/', views.store, name='store'),
]
