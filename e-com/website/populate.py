import os, random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

import django

django.setup()

from home.models import prod

import json, requests

def call_api():
    r = requests.get('https://dummyjson.com/products')
    received_json_data=json.loads(r.text)
    return received_json_data["products"]

def fludit():
    prod_list = call_api()
    for product in prod_list:
        name = product["title"]
        disc = product["description"]
        price = product["price"]
        thumbnail = product["thumbnail"]

        pro = prod.objects.get_or_create(name= name, deisc = disc, price=price, thumbnail=thumbnail)[0]

if __name__ == "__main__":
    print("Populating Script")
    fludit()
    print("populating complete!")

