"""
URL configuration for Janata project.

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
from Table_Apps import views as ta

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ta.view_table, name='view_table'),
    path('graph_view/', ta.graph_view, name='graph_view'),
    path('api/data/', ta.stock_data_api, name='stock_data_api'),
]
