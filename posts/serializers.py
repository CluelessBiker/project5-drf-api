from rest_framework import serializers
from likes.models import Like
from .models import Post


# Class provided by DRF-API walkthrough.
class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for Posts Model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        """
        Restrict size of image upload.
        Produce error warning to inform user.
        """
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image must be smaller than 2MB.')

        if value.image.height > 4096:
            raise serializers.ValidationError('Height must be smaller than 4096px.')

        if value.image.width > 4096:
            raise serializers.ValidationError('Width must be smaller than 4096px.')


