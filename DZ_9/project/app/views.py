from django.shortcuts import render
from django.http import HttpResponse


def index_page(request):
    return render(request, 'app/index.html', {'name': 'LEKI HOME'})


def news_page(request):
    return HttpResponse(
        f"<center>"
        f"<h1>Пока В Разработке</h1>"
        f"<a href='http://127.0.0.1:8000/'>Ввернуть на главную</a>"
        f"</center>"
    )
