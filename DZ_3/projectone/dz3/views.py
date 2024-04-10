from django.shortcuts import render


def index_page(request):
    return render(request, 'index.html')


def game_page(request):
    from random import randint
    from django.http import HttpResponse

    number_one, number_two, number_tree = randint(0, 3), randint(0, 3), randint(0, 3)

    if number_one == number_two == number_tree:
        return HttpResponse(
            f"<h1 style='color: green'>“Победа, все 3 числа равны!”</h1>\n"
            f"\n\n<h3>Вот Сгенерированные числа: <i>{number_one}, {number_two}, {number_tree}</i><h3>"
            f"\n\n\n<center><b style='color: #FF8500'>Чтобы начать заново"
            f"\nОбновите страницу | F5 |</b></center>"
        )
    else:
        return HttpResponse(
            f"<h1 style='color: red'>“Повезет в следующий раз!”</h1>\n"
            f"\n\n<h3>Вот Сгенерированные числа: <i>\t{number_one}, {number_two}, {number_tree}</i></h3>"
            f"\n\n\n<center><b style='color: #FF8500'>Чтобы начать заново"
            f"\nОбновите страницу | F5 |</b></center>"
        )
