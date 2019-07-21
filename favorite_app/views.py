# core Django import
from rest_framework import viewsets
from django.db.models import Q
# local packages
from favorite_app import serializers
from favorite_app.models import Category, FavoriteThings
from favorite_app.utils import validate_id


class CategoryViewSet(viewsets.ModelViewSet):
    """
    Category viewsets
    """

    queryset = Category.objects.all()

    def get_serializer_class(self):
        """
        Conditional render different serializers based on the request
        """

        include_related = self.request.query_params.get('include', None)
        if include_related == 'children':
            return serializers.CategoryWithChildrenSerializer
        return serializers.CategorySerializer


class FavoriteThingsViewSet(viewsets.ModelViewSet):
    """
    FavoriteThings viewsets
    """

    serializer_class = serializers.FavoriteThingsSerializer

    def get_queryset(self):
        """
        custom get queryset method
        """

        category_id = self.request.query_params.get('categoryId', None)
        category_name = self.request.query_params.get('categoryName', None)
        search = self.request.query_params.get('search', None)

        queryset = FavoriteThings.objects.filter()
        if category_id and validate_id(category_id):
            queryset = queryset.filter(category_id=category_id)
        if category_name:
            queryset = queryset.filter(category__name=category_name)
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(description__icontains=search) |
                Q(category__name__icontains=search)
            )

        return queryset
