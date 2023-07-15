from django.core.validators import MinValueValidator
from django.db import models
from users.models import User


class Tag(models.Model):
    """Модель для тегов"""

    name = models.CharField(
        "Тег",
        max_length=200,
        unique=True,
    )
    color = models.CharField(
        "Цвет - HEX",
        max_length=7,
        null=True,
    )
    slug = models.CharField(
        "Slug",
        max_length=200,
        null=True,
        unique=True,
    )

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Тяги"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Модель для ингредиентов"""

    name = models.CharField(
        "Ингридиент",
        max_length=200,
    )
    measurement_unit = models.CharField(
        "Единица измерения",
        max_length=200,
    )

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"
        ordering = ("name",)

    def __str__(self):
        return f"{self.name} {self.measurement_unit}"


class Recipe(models.Model):
    """Модель рецептов"""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="recipes",
        verbose_name="Автор рецепта",
    )
    name = models.CharField(
        "Название",
        max_length=200,
    )
    image = models.ImageField(
        "Картинка",
    )
    text = models.TextField(
        "Описание",
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        verbose_name="Список ингредиентов",
        through="IngredientsAmount",
        related_name="recipes",
    )
    tags = models.ManyToManyField(
        Tag,
        related_name="recipes",
        verbose_name="Тег",
    )
    pub_date = models.DateTimeField(
        "Дата публикации",
        auto_now_add=True,
    )
    cooking_time = models.PositiveSmallIntegerField(
        "Время приготовления (в минутах)",
        validators=[
            MinValueValidator(
                1, message="Время приготовления блюда должно быть больше 0"
            )
        ],
    )

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"
        ordering = ("-pub_date",)

    def __str__(self):
        return self.name


class IngredientsAmount(models.Model):
    """Модель описывающая количество ингридиентов"""

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name="Рецепт",
        related_name="ingredient_amount",
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name="Ингредиент",
        related_name="ingredient_amount",
    )
    amount = models.PositiveSmallIntegerField(
        verbose_name="Количество",
    )

    class Meta:
        verbose_name = "Количество ингридиент"
        verbose_name_plural = "Количество ингридиентов"

    def __str__(self):
        return f"{self.amount} {self.ingredient}"


class Favorite(models.Model):
    """Модель списка избранного"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="favorite",
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name="Рецепт",
        related_name="favorite",
    )

    class Meta:
        verbose_name = "Список избранного"
        verbose_name_plural = "Список избранного"


class ShoppingCart(models.Model):
    """Модель списка избранного"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="shopping_cart",
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name="Рецепт",
        related_name="shopping_cart",
    )

    class Meta:
        verbose_name = "Список покупок"
        verbose_name_plural = "Список покупок"
