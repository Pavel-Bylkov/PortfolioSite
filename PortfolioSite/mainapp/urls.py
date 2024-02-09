"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from mainapp import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('id<int:id>', views.home, name='home'),
    path('edit', views.setprofile, name='setprofile'),
    path('edit2', views.setprofile2, name='setprofile2'),
    path('change', views.change, name='change'),
]
