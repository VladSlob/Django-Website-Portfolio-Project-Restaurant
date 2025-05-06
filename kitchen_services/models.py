from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Dish type"
        verbose_name_plural = "Dish types"
        ordering = ("name", )

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(45)]
    )

    class Meta:
        ordering = ("-years_of_experience", )

    def __str__(self):
        return f"{self.username}: ({self.first_name} {self.last_name})"


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(
        decimal_places=2,
        max_digits=6,
        validators=[MinValueValidator(0.01), MaxValueValidator(1000)]
    )
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, related_name="dishes")
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cooked_dishes")

    class Meta:
        verbose_name_plural = "Dishes"
        ordering = ("price", )

    def __str__(self):
        return self.name
