from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from kitchen_services.models import DishType, Dish


class ModelTests(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="test")
        self.assertEqual(str(dish_type), dish_type.name)

    def test_cook_str(self):
        cook = get_user_model().objects.create(
            username="test.test",
            first_name="Test",
            last_name="Test",
        )
        self.assertEqual(str(cook),f"{cook.username}: ({cook.first_name} {cook.last_name})")

    def test_dish_str(self):
        dish_type = DishType.objects.create(name="test")
        dish = Dish.objects.create(
            name="test",
            description="test description",
            price=5.00,
            dish_type=dish_type,
        )
        self.assertEqual(str(dish), dish.name)

    def test_create_cook_with_years_of_experience(self):
        username = "test.test"
        years_of_experience = 20
        cook = get_user_model().objects.create_user(
            username=username,
            years_of_experience=years_of_experience,
        )
        self.assertEqual(cook.username, username)
        self.assertEqual(cook.years_of_experience, years_of_experience)
