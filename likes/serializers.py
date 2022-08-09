from django.db import IntegrityError
from rest_framework import serializers
from likes.models import Like


# Class provided by DRF-API walkthrough.
class LikeSerializer(serializers.ModelSerializer):
    """
    Likes model serializer.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = [
            'id',
            'created_on',
            'owner',
            'post',
        ]

    def create(self, validated_data):
        """
        Supplies an error message should
        the user attempt to like the same
        post more than once.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
