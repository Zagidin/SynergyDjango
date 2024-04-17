from django.shortcuts import render


def index_page(request):
    name = "Главная страница"
    return render(request, 'app/index.html', {'name': name})


def about_page(request):
    name = "Страница отзывов"
    return render(request, 'app/about.html', {'name': name})


def news_page(request):
    name = "Новостная страница"
    return render(request, 'app/news.html', {'name': name})
