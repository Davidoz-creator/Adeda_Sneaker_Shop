from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, 'accounts/index.html')

def login(request):
    return render (request, 'accounts/login.html')    

def product_detail (request):
    return render (request, 'accounts/product_detail.html') 

def product_grid (request):
    return render (request, 'accounts/product_grid.html')     

def register (request):
    return  render(request, 'accounts/register.html')  

def profile (request):
    return render(request,'accounts/profile.html') 

def contact(request):
    return render(request, 'accounts/contact.html')

def thanks (request):
    return render(request, 'public/thanks.html') 

def login (request):
    return render(request,'public/login.html')            