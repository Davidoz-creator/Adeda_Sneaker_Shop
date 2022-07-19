from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .import views

from .views import home


app_name = "public"

urlpatterns = [
     # Beginning Reset password
     path('', home, name="home"),
     path('login/',views.login, name="login"),
     path('product_detail/',views.product_detail, name="product_detail"),
     path('register/', views.register, name="register"),
     path('profile/', views.profile, name='profile'),
     path('contact',views.contact, name='contact'),
     path('thanks/',views.thanks, name='thanks'),
     path('product_grid/',views.product_grid, name="product_grid"),
     path('login',views.login,name='login'),
     
     
     ]

 