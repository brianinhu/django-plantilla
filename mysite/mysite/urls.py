"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('home', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('articles', views.articles, name='articles'),
    path('v_create_article', views.v_create_article, name='v_create_article'),
    path('f_create_article', views.f_create_article, name='f_create_article'),
    path('v_edit_article/<int:article_id>', views.v_edit_article, name='v_edit_article'),
    path('f_edit_article', views.f_edit_article, name='f_edit_article'),
    path('f_delete_article/<int:article_id>', views.f_delete_article, name='f_delete_article'),
]
