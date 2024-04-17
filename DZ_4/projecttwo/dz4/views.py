from django.shortcuts import render
from django.http import HttpResponse
from random import randint


slova_text = [
    'Привет!', 'Здарова!', 'Пpиветики - Пистолетики!',
    'Синергия', 'Degestan-05', 'Rostov-on-Don', 'Молодец!'
]


def index_page(request):
    return render(request, 'index.html')


def pages_page(request):
    return render(request, 'pages.html')


def page_one(request):
    return HttpResponse(
        f"<h2>Рандомные 2 слова...</h2>"
        f"<center>"
        f"<h4>{slova_text[randint(0, 2)]}</h4>"
        f"<h4>{slova_text[randint(0, 2)]}</h4>"
        f"</center>"
        f"\n\n\n\n\n<p>Перейти на страницу Page2  --  <a href='http://127.0.0.1:8000/pages/page2'>page2</a></p>"
    )

def page_two(request):
    return HttpResponse(
        f"<h2>Рандомные 2 слова...</h2>"
        f"<center>"
        f"<h4>{slova_text[randint(3, 6)]}</h4>"
        f"<h4>{slova_text[randint(3, 6)]}</h4>"
        f"</center>"
        f"\n\n\n\n\n<p>Перейти на страницу Page1  --  <a href='http://127.0.0.1:8000/pages/page1'>page1</a></p>"
    )
