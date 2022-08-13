from django.shortcuts import render
from django.http import HttpResponse
import requests


def hello_page(request):
    return HttpResponse('Hello!')


def dish(request, dish_name):

    servings = int(request.GET.get('servings', '1'))

    recipes = {
        'omelette': {
            'яйца, шт': 2*servings,
            'молоко, л': format(0.1*servings, ".1g"),
            'соль, ч.л.': format(0.5*servings, ".1g"),
        },
        'pasta': {
            'макароны, г': format(0.3*servings, ".1g"),
            'сыр, г': format(0.05*servings, ".1g"),
        },
        'buter': {
            'хлеб, ломтик': 1*servings,
            'колбаса, ломтик': 1*servings,
            'сыр, ломтик': 1*servings,
            'помидор, ломтик': 1*servings,
        },
        # можете добавить свои рецепты ;)
    }

    context = {'recipes': recipes[dish_name]}

    return render(request, 'calculator/index.html', context)
