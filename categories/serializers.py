from rest_framework import serializers
from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """
    Category serializer model.
    """
    category = serializers.ReadOnlyField(source='category.category')

    class Meta:
        """
        Display fields.
        """
        model = Category
        fields = [
            'id',
            'created_on',
            'category',
        ]
