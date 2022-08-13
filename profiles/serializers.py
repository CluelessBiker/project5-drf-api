from rest_framework import serializers
from .models import Profile
from followers.models import Follower


# Class provided by DRF-API walkthrough.
class ProfileSerializer(serializers.ModelSerializer):
    """
    Profile serializer.
    Providing readability to profile data in API.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    posts_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        """
        Associates User to User Profile.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        """
        Returns following count for individual user
        """
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user,
                followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    class Meta:
        """
        Lists of Profile model fields to display.
        """
        model = Profile
        fields = [
            'id',
            'owner',
            'created_on',
            'modified_on',
            'description',
            'image',
            'first_name',
            'last_name',
            'username',
            'country',
            'is_owner',
            'following_id',
            'followers_count',
            'following_count',
            'posts_count',
        ]
