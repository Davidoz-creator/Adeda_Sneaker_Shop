from django.shortcuts import render
from django.views.generic import ListView 
from .models import Product 
from .models import Destiny


# Create your views here.
def home(request):
    return render (request, 'accounts/index.html')


class ProductList(ListView):
     model = Product    

class DestinyList(ListView):
    model = Destiny

