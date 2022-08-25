from rest_framework import generics, permissions, filters
from p5_drf_api.permissions import IsOwnerOrReadOnly
from .models import Event
from .serializers import EventSerializer


class EventList(generics.ListCreateAPIView):
    """
    Retrieve events from DB.
    Create new events.
    """
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.all()

    def perform_create(self, serializer):
        """
        Check for user authentication.
        """
        serializer.save(owner=self.request.user)

        filter_backends = [
            filters.SearchFilter,
        ]

        search_fields = [
            'owner__username',
            'title',
            'city',
            'country',
        ]


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update & Destroy events.
    """
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.all()
