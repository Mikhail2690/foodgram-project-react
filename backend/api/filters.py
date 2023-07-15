from django_filters import rest_framework as filters
from recipes.models import Recipe


class RecipeFilter(filters.FilterSet):
    """Фильтр для тегов"""

    tags = filters.CharFilter(field_name="tags__name", lookup_expr="icontains")

    class Meta:
        model = Recipe
        fields = ["tags"]
