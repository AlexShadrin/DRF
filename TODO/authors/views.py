from django.shortcuts import render
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
# Create your views here.

from authors.filters import BookFilter
from .models import Author, Biographies, Book
from .serializers import AuthorModelSerializer, BiographiesHyperlinkedModelSerializer, BookModelSerializer

class AuthorModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer

class BiographiesModelViewSet(ModelViewSet):
    queryset = Biographies.objects.all()
    serializer_class = BiographiesHyperlinkedModelSerializer

class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

class BookDjangoFilterViewSet(ModelViewSet):
   queryset = Book.objects.all()
   serializer_class = BookModelSerializer
   # filterset_fields = ['id','name']
   filterset_class = BookFilter

class BookLimitOffsetPagination(LimitOffsetPagination):
   default_limit = 20

class BookLimitOffsetPaginatonViewSet(ModelViewSet):
   # renderer_classes = [JSONRenderer]
   queryset = Book.objects.all()
   serializer_class = BookModelSerializer
   pagination_class = BookLimitOffsetPagination
