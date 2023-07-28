from django_filters.rest_framework import AllValuesMultipleFilter, FilterSet

from recipes.models import Recipe
from rest_framework.filters import SearchFilter


class RecipeFilter(FilterSet):
    """Фильтр для тегов"""

    tags = AllValuesMultipleFilter(field_name="tags__slug", label="tags")

    class Meta:
        model = Recipe
        fields = ("tags",)


class IngredientFilter(SearchFilter):
    """Фильтр для ингредиентов"""
    search_param = 'name'
