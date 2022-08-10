from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


# Class provided by DRF-API walkthrough.
class CommentSerializer(serializers.ModelSerializer):
    """
    Comment Model serializer.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_on = serializers.SerializerMethodField()
    modified_on = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Associate comment to user ID.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        """
        Display time elapsed since comment created.
        """
        return naturaltime(obj.created_on)

    def get_updated_at(self, obj):
        """
        Display time elapsed since comment modified.
        """
        return naturaltime(ob.modified_on)

    class Meta:
        """
        Return fields to display.
        """
        model = Comment
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'post',
            'created_on',
            'modified_on',
            'content',
        ]


# Class provided by DRF-API walkthrough.
class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for comment detail view.
    """
    post = serializers.ReadOnlyField(source='post.id')
