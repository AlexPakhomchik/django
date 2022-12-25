"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path, include

from abi import views

other_patterns = [
    re_path(r'^first_page', views.first_page, kwargs={'name': 'John Wick', 'place': 'Continental'}),
    path('second_page', views.second_page),
    path('second_page/<str:santa>', views.second_page),
    path('second_page/<str:santa>/<str:place>', views.second_page),

]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('other/', include(other_patterns)),
]
