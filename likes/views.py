from rest_framework import generics, permissions
from p5_drf_api.permissions import IsOwnerOrReadOnly
from likes.models import Like
from likes.serializers import LikeSerializer


# Class provided by DRF-API walkthrough.
class LikeList(generics.ListCreateAPIView):
    """
    Provide logged in users the ability
    to like/unlike a post.
    """
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        """
        If user is authenticated, like/dislike
        will be saved to database
        """
        serializer.save(owner=self.request.user)


# Class provided by DRF-API walkthrough.
class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    The ability to create/delete
    a like.
    """
    permissions_classes = [IsOwnerOrReadOnly]
    serilaizer_class = LikeSerializer
    queryset = Like.objects.all()
