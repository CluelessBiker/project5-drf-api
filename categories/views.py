from rest_framework import generics, permissions
from categories.models import Category
from categories.serializers import CategorySerializer


class CategoryList(generices.ListCreateAPIView):
    """
    Category list.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetail(generics.RetrieveAPIView):
    """
    View category.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
