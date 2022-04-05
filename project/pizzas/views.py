from django.shortcuts import render
from pizzas.models import Pizza


def home(request):
    pizzas = Pizza.objects.all().prefetch_related("toppings").order_by("price")
    return render(request, "pizzas/home.html", {"pizzas": pizzas})
