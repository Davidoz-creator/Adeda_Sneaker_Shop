from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .import views

from .views import home

urlpatterns=[
path('', home, name="home"),

]