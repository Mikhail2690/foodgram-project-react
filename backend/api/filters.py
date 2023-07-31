from django_filters.rest_framework import (AllValuesMultipleFilter,
                                           FilterSet, ModelChoiceFilter)

from recipes.models import Recipe, User
from rest_framework.filters import SearchFilter


class RecipeFilter(FilterSet):
    """Фильтр для рецептов по тегам и автору"""

    tags = AllValuesMultipleFilter(field_name="tags__slug", label="tags")
    author = ModelChoiceFilter(queryset=User.objects.all())

    class Meta:
        model = Recipe
        fields = ("author", "tags",)


class IngredientFilter(SearchFilter):
    """Фильтр для ингредиентов"""
    search_param = "name"
