from django.shortcuts import render
from home.models import prod

def index(request):
    products = prod.objects.order_by("name")
    dict = {"prod":products}
    return render(request, "home/index.html", context = dict)