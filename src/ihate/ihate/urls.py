"""ihate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from persons.views import Proprio_usuarioView, Create_pessoaView, Delete_pessoaView, Pessoa_loginView, Lista_pessoasView

app_name = 'persons'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pessoas/<int:id>/', Proprio_usuarioView.as_view()),
    path('pessoas/create', Create_pessoaView.as_view()),
    path('pessoas/<int:id>/delete', Delete_pessoaView.as_view()),
    path('pessoas/login', Pessoa_loginView.as_view(),name="home"),
    path('lista_pessoas', Lista_pessoasView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)