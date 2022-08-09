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
    queryset = Profile.objects.all()


# Class provided by DRF-API walkthrough.
class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update Profile fields if Owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
