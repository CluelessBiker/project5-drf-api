from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Profile
from .serializers import ProfileSerializer
from p5_drf_api.permissions import IsOwnerOrReadOnly


# Class provided by DRF-API walkthrough.
class ProfileList(generics.ListAPIView):
    """
    List all created profiles.
    """
    serializer_class = ProfileSerializer

    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_on')

    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile',
    ]

    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_on',
        'owner__followed__created_on',
    ]


# Class provided by DRF-API walkthrough.
class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update Profile fields if Owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer

    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('created_on')
