from django.shortcuts import render
from django.http import HttpResponse


def index_page(request):
    name = {
        'name': 'Главаная страница'
    }
    
    return render(request, 'app/index.html', name)


def picture_page(request):
    name = {
        'name': 'Фото'
    }
    
    return render(request, 'app/picture.html', name)
