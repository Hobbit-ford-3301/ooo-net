from django.shortcuts import render
from django.http import HttpResponse


def hello_page(request):
    return HttpResponse('Hello!')


def dish(request, dish_name):

    servings = int(request.GET.get('servings', '1'))

    recipes = {
        'omelette': {
            'яйца, шт': 2,
            'молоко, л': 0.1,
            'соль, ч.л.': 0.5,
        },
        'pasta': {
            'макароны, г': 0.3,
            'сыр, г': 0.05,
        },
        'buter': {
            'хлеб, ломтик': 1,
            'колбаса, ломтик': 1,
            'сыр, ломтик': 1,
            'помидор, ломтик': 1,
        },

    }

    for item in recipes[dish_name]:
        new_amount = recipes[dish_name][item] * servings
        recipes[dish_name][item] = new_amount

    context = {'recipes': recipes[dish_name]}

    return render(request, 'calculator/index.html', context)
