"""audit URL Configuration

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
from django.urls import path
from licitacao.views import home, licitacoes, aviso, julgamento, homologada, denuncia, obrigado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('licitacoes/', licitacoes, name='url_licitacoes'),
    path('aviso/', aviso, name='url_aviso'),
    path('julgamento/', julgamento, name='url_julgamento'),
    path('homologada/', homologada, name='url_homologada'),
    path('denuncia/', denuncia, name='url_denuncia'),
    path('obrigado/', obrigado, name='url_obrigado'),
    path('', home, name='url_home'),
]
