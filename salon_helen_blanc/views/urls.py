"""salon_helen_blanc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from salon_helen_blanc.views.index import index
from salon_helen_blanc.views.home import home
from salon_helen_blanc.views.calendar import load_calendar
from salon_helen_blanc.views.picture import picture
from salon_helen_blanc.views.contact import contact

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', index),    
    path('home.html', home, name="home"),
    path('index.html', index, name="index"),
    path('calendar.html', load_calendar, name="calendar"),
    path('picture.html', picture, name="picture"),
    path('contact.html', contact, name="contact"),    
]