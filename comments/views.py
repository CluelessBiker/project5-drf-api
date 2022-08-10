from rest_Framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend§
from p5_drf_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


# Class provided by DRF-API walkthrough.
class CommentList(generics.ListCreateAPIView):
    """
    Create & Retrieve comments.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    filter_backends = [
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'post',
    ]

    def perform_create(self, serializer):
        """
        Save comment to user details.
        If user is authenticated."
        """
        serializer.save(owner='self.request.user')


# Class provided by DRF-API walkthrough.
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, destroy comment.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all
