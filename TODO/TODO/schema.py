import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType
from authors.models import Author,Book


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = '__all__'

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = '__all__'

class Query(ObjectType):

    author_by_id = graphene.List(AuthorType,id=graphene.Int(required=False))

    def resolve_author_by_id(root,info,id=None):
        if id:
            return Author.objects.get(id=id)
        return Author.objects.all()

    book_by_author = graphene.List(BookType,first_name=graphene.String(required=False))

    def resolve_book_by_author(root,info,first_name=None):
        if first_name:
            return Book.objects.filter(authors__first_name=first_name)
        return Book.objects.all()



schema = graphene.Schema(query=Query)



#
# class AuthorType(DjangoObjectType):
#     class Meta:
#         model = Author
#         fields = '__all__'
#
#     @classmethod
#     def mutate(cls, root, info, **kwargs):
#         author = Author.objects.create(**kwargs)
#         return AuthorCreateMutation(author=author)
#
# class AuthorUpdateMutation(graphene.Mutation):
#     class Arguments:
#
#         birthday_year = graphene.Int(required=True)
#         id = graphene.ID()
#
#     author = graphene.Field(AuthorType)
#
#     @classmethod
#     def mutate(cls, root, info, **kwargs):
#         author = Author.objects.get(id=kwargs.get('id'))
#         author.birthday_year =kwargs.get('birthday_year')
#         author.save()
#         return cls(author=author)
#
# class AuthorCreateMutation(graphene.Mutation):
#     class Arguments:
#         first_name = graphene.String()
#         last_name = graphene.String()
#         birthday_year = graphene.Int(required=True)
#
#     author = graphene.Field(AuthorType)
#
#     @classmethod
#     def mutate(cls,root,info,**kwargs):
#         author = Author.objects.create(**kwargs)
#         return cls(author=author)
#
# class AuthorDeleteMutation(graphene.Mutation):
#     class Arguments:
#         id = graphene.ID()
#
#     authors = graphene.List(AuthorType)
#
#     @classmethod
#     def mutate(cls, root, info, **kwargs):
#         Author.objects.get(id=kwargs.get('id')).delete()
#         return cls(authors=Author.objects.all())
#
# class Mutations(ObjectType):
#     update_author = AuthorUpdateMutation.Field()
#     create_author = AuthorCreateMutation.Field()
#     delete_author = AuthorDeleteMutation.Field()
#
# schema = graphene.Schema(mutation=Mutations)