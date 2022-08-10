from rest_framework import generics, permissions, filters
from p5_drf_api.permissions import IsOwnerOrReadOnly
from .models import Article
from .serializers import ArticleSerializer


class ArticleList(generics.ListCreateAPIView):
    """
    Create new article.
    """
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Article.objects.all()

    def perform_create(self, serializer):
        """
        If user is authenticated,
        save article.
        """
        serializer.save(owner=self.request.user)

    filter_backends = [
        filters.SearchFilter,
    ]

    search_fields = [
        'owner__username',
        'title',
    ]


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, destroy article.
    """
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Article.objects.all()
