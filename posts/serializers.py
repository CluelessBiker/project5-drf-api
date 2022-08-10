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

        return value

    def get_is_owner(self, obj):
        """
        Return correct user.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        """
        Return & calculate total number
        of likes on post view.
        """
        user = self.context['request'].user

        if user.is_authenticated:
            like = Likes.objects.filter(
                owner=user,
                post=obj
            ).first()
            return like.id if like else None

        return None

    
