"""
URL configuration for seedcase_portal project.

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
from django.contrib import admin
from django.urls import path
from .views import home, VariableList, ProjectList


# Setup the relative url path for the pages
urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('variables/', VariableList, name='variable-list'),
    path('projects/', ProjectList.as_view(), name='project-list'),
]

admin.site.index_title = "Seedcase Registry Administration"
admin.site.site_header = "Seedcase Registry Administration"
admin.site.site_title = "Seedcase Registry Administration"
