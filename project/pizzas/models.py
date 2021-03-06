from django.db import models
from django.db.models import Case, OuterRef, Subquery, Value, When


class Topping(models.Model):
    VEGAN = 0
    VEGETARIAN = 1
    NON_VG_NON_V = 2
    TOPPING_TYPE_CHOICES = (
        (VEGAN, "Vegan-friendly"),
        (VEGETARIAN, "Vegetarian-friendly"),
        (NON_VG_NON_V, "Non-vegan non-veg"),
    )
    name = models.CharField(max_length=64)
    rating = models.PositiveSmallIntegerField(choices=TOPPING_TYPE_CHOICES)

    def __str__(self):
        return self.name


class PizzaManager(models.Manager):
    def get_queryset(self):
        max_rating_subquery = (
            Pizza.toppings.through.objects.filter(pizza_id=OuterRef("id"))
            .values("topping__rating")
            .order_by("-topping__rating")[:1]
            .values_list("topping__rating", flat=True)
        )
        return (
            super()
            .get_queryset()
            .annotate(
                max_rating=Subquery(max_rating_subquery),
                is_vegan=Case(
                    When(max_rating=Topping.VEGAN, then=Value(True)),
                    default=Value(False),
                    output_field=models.BooleanField(),
                ),
                is_vegetarian=Case(
                    When(max_rating__lte=Topping.VEGETARIAN, then=Value(True)),
                    default=Value(False),
                    output_field=models.BooleanField(),
                ),
            )
        )


class Pizza(models.Model):
    name = models.CharField(max_length=64)
    toppings = models.ManyToManyField(Topping)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name

    objects = PizzaManager()
