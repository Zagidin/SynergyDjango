from django.shortcuts import render


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
