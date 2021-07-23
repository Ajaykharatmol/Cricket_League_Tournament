from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
#from .models import Books
#from .forms import BooksForm
from django.template import Context
from django.shortcuts import render
import requests

#def index(request):
    #emp = Books.objects.all()
    #return render(request,'dashboard.html')

def index(request):
    res = requests.get('http://127.0.0.1:8000/Cricket_Tournament_API/countries/')

    response_data = res.json()
    
    #print(response_data)
    products = response_data[0]
    print(products)
   
    if res.status_code == 200:
        return render(request, 'dashboard.html',
                      {"products": products})
    else:
        print("error")
    
