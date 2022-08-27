from django.http import HttpResponse
from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    phones = Phone.objects.all()
    context = {'phones': phones}
    return render(request, template, context)


def show_me_my_phones(request):

    phones_obj = Phone.objects.all()
    phones = [f'{ph.name}: {ph.price}' for ph in phones_obj]
    return HttpResponse('<br>'.join(phones))

def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
