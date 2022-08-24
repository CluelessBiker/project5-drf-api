from rest_framework import serializers
from .models import Article
# from categories.models import Category


class ArticleSerializer(serializers.ModelSerializer):
    """
    Serializer for Articles model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    # display_category = serializers.ReadOnlyField(source='category.name')
    # category = serializers(source='category.name')

    # category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    # category = serializers.RelatedField.to_representation(
    #     source='category',
    #     read_only=True
    # )
    # category = serializers.PrimaryKeyRelatedField(source='category.name')
    # category = serializers.ReadOnlyField(source='category.name')
    # category = serializers.RelatedField(source='category.name')
    # category_props = PropsSerializer(read_only=True, many=True)
    # category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # category = serializers.CharField(source="category.name", write_only=True)
    # category = serializers.SerializerMethodField()

    def validate_image(self, value):
        """
        Restrict size of image upload.
        Produce error warning to inform user.
        """
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError(
                'Image must be smaller than 2MB.')

        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Height must be smaller than 4096px.')

        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Width must be smaller than 4096px.')

        return value

    def get_is_owner(self, obj):
        """
        Return correct user.
        """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """
        Display fields for views.
        """
        model = Article
        fields = [
            'id',
            'owner',
            'is_owner',
            'title',
            'content',
            'image',
            'image_credit',
            'category',
            'created_on',
            'modified_on',
            'profile_id',
            'profile_image',
        ]
