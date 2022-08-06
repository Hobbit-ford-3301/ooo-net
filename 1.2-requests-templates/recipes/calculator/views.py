from django.shortcuts import render
from django.http import HttpResponse
import requests

DATA = {
    'omlet': {
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
    # можете добавить свои рецепты ;)
}


def hello_page(request):
    return HttpResponse('Hello!')


def omelette(request):

    servings = int(request.GET.get('servings', '1'))

    context = {
        'omelette': {
            'яйца, шт': 2*servings,
            'молоко, л': 0.1*servings,
            'соль, ч.л.': 0.5*servings,
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
        # можете добавить свои рецепты ;)
    }

    return render(request, 'calculator/omelette.html', context)


def pasta(request):

    servings = int(request.GET.get('servings', '1'))

    context = {
        'omelette': {
            'яйца, шт': 2,
            'молоко, л': 0.1,
            'соль, ч.л.': 0.5,
        },
        'pasta': {
            'макароны, г': 0.3 * servings,
            'сыр, г': 0.05 * servings,
        },
        'buter': {
            'хлеб, ломтик': 1,
            'колбаса, ломтик': 1,
            'сыр, ломтик': 1,
            'помидор, ломтик': 1,
        },
    }

    return render(request, 'calculator/pasta.html', context)


def buter(request):

    servings = int(request.GET.get('servings', '1'))

    context = {
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
            'хлеб, ломтик': 1 * servings,
            'колбаса, ломтик': 1 * servings,
            'сыр, ломтик': 1 * servings,
            'помидор, ломтик': 1 * servings,
        },
    }

    return render(request, 'calculator/buter.html', context)