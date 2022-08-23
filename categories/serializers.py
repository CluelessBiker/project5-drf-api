from rest_framework import serializers
from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """
    Category serializer model.
    """
    name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        """
        Display fields.
        """
        model = Category
        fields = [
            'id',
            'created_on',
            'name',
        ]
