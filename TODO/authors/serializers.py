from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Author, Biographies, Book

class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class AuthorCustomModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ('first_name',)

class BiographiesHyperlinkedModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Biographies
        fields = '__all__'

class BookModelSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookCustomModelSerializer(ModelSerializer):
    authors = AuthorModelSerializer()
    class Meta:
        model = Book
        fields = '__all__'