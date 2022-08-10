from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from p5_drf_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


# Class provided by DRF-API walkthrough.
class PostList(generics.ListCreateAPIView):
    """
    Retrieve & Create new posts.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_on')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
    ]

    search_fields = [
        'owner__username',
        'title',
    ]

    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_on',
    ]

    def perform_create(self, serializer):
        """
        Check user logged in & authenticated.
        If so, save new post to database.
        """
        serializer.save(owner=self.request.user)


# Class provided by DRF-API walkthrough.
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Function to Retrieve,
    Edit, Delete post if owner.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True)
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_on')
