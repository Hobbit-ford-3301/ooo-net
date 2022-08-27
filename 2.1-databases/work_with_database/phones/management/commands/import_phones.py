import csv

from django.utils.text import slugify

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

            for item in phones:
                phone = Phone()
                phone.id = item['id'],
                phone.name = item['name'],
                phone.price = item['price'],
                phone.image = item['image'],
                phone.release_date = item['release_date'],
                phone.lte_exists = item['lte_exists'],
                phone.slug = slugify(item['name'])


