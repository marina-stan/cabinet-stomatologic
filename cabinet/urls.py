"""cabinet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('contact/', views.contact, name = 'contact'),
    path('about/', views.about, name = 'about'),
    path('consultatii-online', views.contactsendemail, name = 'consultatii'),
    path('conectare/', views.conectare, name = 'conectare'),
    path('logout/', views.logout, name = 'logout'),
    path('medici/', views.medici, name = 'medici'),
    path('asistenti/', views.asistenti, name = 'asistenti'),
    path('contul-meu/', views.contulMeu, name = 'contul-meu'),
    path('adaugapacient/', views.adaugapacient, name = 'adaugapacient'),
    path('adaugaprogramare/', views.adaugaprogramare, name = 'adaugaprogramare'),
    path('adaugafisa/', views.adaugafisa, name = 'adaugafisa'),
    path('adaugaprodus/', views.adaugaprodus, name = 'adaugaprodus'),
    path('adaugafactura/', views.adaugafactura, name = 'adaugafactura'),
    path('adaugadiagnostic/', views.adaugadiagnostic, name = 'adaugadiagnostic'),
    path('adaugatratament/', views.adaugatratament, name = 'adaugatratament'),
    path('adaugaprogramarepacient/', views.adaugaprogramarepacient, name = 'adaugaprogramarepacient'),
    path('pdf1/', views.render_pdf_view, name = 'pdf1'),
    path('facturi/', views.FacturaListView.as_view(), name = 'facturi-list-view'),
    path('pdf/<pk>/', views.factura_render_pdf_view, name = 'facturi-pdf-view'),
    path('editeazapacient/<pk>/', views.editeazapacient, name = 'editeazapacient'),
    path('fise-pacienti/', views.FisaPacientListView.as_view(), name = 'fisa-pacient-list-view'),
    path('pdf-fisa/<pk>/', views.fisaPacientView, name = 'fisa-pacient-view'),
    path('fisa-consultatii/<pk>', views.fisaConsultatii, name = 'fisa-consultatii'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
