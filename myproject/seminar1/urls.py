"""
URL configuration for django_seminars project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path, include
from seminar1 import views

urlpatterns = [
    path('', views.seminar1, name='seminar1'),
    path('heads_tails/', views.heads_tails, name='heads_tails'),
    path('dice/', views.dice, name='dice'),
    path('rand/', views.rand, name='rand'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
]