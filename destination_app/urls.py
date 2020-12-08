"""BookMyGuide URL Configuration

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
from .views import *

app_name = 'destination'

urlpatterns = [
    path('findaguide/', findaguide, name='findaguide'),
    path('annapurna/', annapurna, name='annapurna'),
    path('everest/', everest, name='everest'),
    path('kathmandu/', kathmandu, name='kathmandu'),
    path('bhaktapur/', bhaktapur, name='bhaktapur'),
    path('hireform/', hireform, name='hireform'),
    path('treksandtours/', trekandtour, name='trekandtour'),
    path('mytours/', tour, name='tour'),
    path('richa/', richa, name='richa'),
    path('trek/annapurna/', anna, name='anna')
]
