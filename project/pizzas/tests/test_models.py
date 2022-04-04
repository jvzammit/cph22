from django.test import TestCase
from model_bakery import baker
from pizzas.models import Pizza
from pizzas.tests.utils import load_data


class ToppingTest(TestCase):
    def test_str(self):
        topping = baker.make("pizzas.Topping", name="tomato sauce")
        self.assertEqual(str(topping), "tomato sauce")


class PizzaTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        load_data()

    def test_str(self):
        topping = baker.make(Pizza, name="napoletana")
        self.assertEqual(str(topping), "napoletana")

    def test_is_vegan(self):
        rossa = Pizza.objects.get(name="rossa")
        self.assertTrue(rossa.is_vegan)
        bianca = Pizza.objects.get(name="bianca")
        self.assertFalse(bianca.is_vegan)
        margherita = Pizza.objects.get(name="margherita")
        self.assertFalse(margherita.is_vegan)
        capricciosa = Pizza.objects.get(name="capricciosa")
        self.assertFalse(capricciosa.is_vegan)
        diablo = Pizza.objects.get(name="diablo")
        self.assertFalse(diablo.is_vegan)
        campagnola = Pizza.objects.get(name="campagnola")
        self.assertTrue(campagnola.is_vegan)

    def test_is_vegetarian(self):
        rossa = Pizza.objects.get(name="rossa")
        self.assertTrue(rossa.is_vegetarian)
        bianca = Pizza.objects.get(name="bianca")
        self.assertTrue(bianca.is_vegetarian)
        margherita = Pizza.objects.get(name="margherita")
        self.assertTrue(margherita.is_vegetarian)
        capricciosa = Pizza.objects.get(name="capricciosa")
        self.assertFalse(capricciosa.is_vegetarian)
        diablo = Pizza.objects.get(name="diablo")
        self.assertFalse(diablo.is_vegetarian)
        campagnola = Pizza.objects.get(name="campagnola")
        self.assertTrue(campagnola.is_vegetarian)
