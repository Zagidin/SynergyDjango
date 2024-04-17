from django.shortcuts import render
from .models import Manufacturer, Category


def index_page(request):
    category_tovara = Category.objects.all()
    
    data = {
        "categori": category_tovara,
    }
    
    return render(request, 'app/index.html', data)


def about_page(request):
    proizvoditel_tovara = Manufacturer.objects.all()
    
    return render(request, 'app/proizvoditel.html', {"proizvoditel": proizvoditel_tovara}) 
