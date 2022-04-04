from django.db import models


class Topping(models.Model):
    VEGAN = 0
    VEGETARIAN = 1
    TOPPING_TYPE_CHOICES = (
        (VEGAN, "Vegan-friendly"),
        (VEGETARIAN, "Vegetarian-friendly"),
    )
    name = models.CharField(max_length=64)
    rating = models.PositiveSmallIntegerField(
        blank=True, null=True, choices=TOPPING_TYPE_CHOICES
    )

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=64)
    toppings = models.ManyToManyField(Topping)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name

    @property
    def is_vegan(self):
        return all([topping.rating == Topping.VEGAN for topping in self.toppings.all()])

    @property
    def is_vegetarian(self):
        return all(
            [
                topping.rating in (Topping.VEGAN, Topping.VEGETARIAN)
                for topping in self.toppings.all()
            ]
        )
