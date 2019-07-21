
# core Django import
from django.utils import timezone
from rest_framework import serializers
# Local import
from favorite_app.models import Category, FavoriteThings
from favorite_app.utils import re_order_ranking, gnerate_audit_log
from favorite_app.constants import constant_messages


class CategorySerializer(serializers.ModelSerializer):
    """
    Category serializer. Serializes and deserializes category data
    """

    class Meta:
        model = Category
        fields = ('id', 'name', 'favorite_in_category_count')


class FavoriteThingsSerializer(serializers.ModelSerializer):
    """
    FavoriteThings serializer. Serializes and deserializes FavoriteThings data
    """

    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="category", write_only=True)
    category = CategorySerializer(read_only=True, required=False)

    class Meta:
        model = FavoriteThings
        fields = (
            'id',
            'title',
            'description',
            'ranking',
            'category_id',
            'metadata',
            'audit_log',
            'created_date',
            'modified_date',
            'category')

    def create(self, validated_data):
        """
        Overide serializers create method

        Parameters:
            validated_data: contains serializers validated data
        """

        request = self.context['request']
        re_order_ranking(validated_data, request)
        return FavoriteThings.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Custom update for the resource management.
        Parameters:
            validated_data: contains serializers validated data
            instance: current data to be updated
        """

        request = self.context['request']

        if instance.ranking != validated_data.get('ranking'):
            re_order_ranking(validated_data, request)\

        audit_log = gnerate_audit_log(instance, validated_data)
        validated_data['audit_log'] = audit_log
        validated_data['modified_date'] = timezone.now()
        instance = super(FavoriteThingsSerializer, self).update(instance,
                                                                validated_data)
        return instance

    def validate_description(self, description):
        """
        validates description field

        Parameters:
            description: contains serializers description data
        """

        if description:
            if len(description) < 10:
                raise serializers.ValidationError(
                    constant_messages['invalid_desciption'])
        return description


class CategoryWithChildrenSerializer(serializers.ModelSerializer):
    """
    Category serializer. Serializes and deserializes category data

    Return:
       category data with its associated favoritethings
    """

    categories = FavoriteThingsSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'categories')
