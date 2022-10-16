from django import db
from django.test import TestCase
#

from rest_framework import status
from rest_framework.test import APIRequestFactory,force_authenticate,APIClient,APISimpleTestCase,APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User

from .views import AuthorModelViewSet
from .models import Author,Biographies,Book


class TestAuthorViewSet(TestCase):



    def setUp(self) -> None:
        self.url = '/api/authors/'
        self.authors_dict = {'first_name':'Александр','last_name':'Пушкин','birthday_year':1799}
        self.authors_dict_fake = {'first_name':'Имя','last_name':'Фамилия','birthday_year':2000}
        self.format = 'json'
        self.login = 'admin'
        self.password = 'admin__12345678'
        self.admin = User.objects.create_superuser(self.login,'admin@mail.ru',self.password)
        self.authors = Author.objects.create(**self.authors_dict)


    def test_factory_get_list(self):
        factory = APIRequestFactory()
        request = factory.get(self.url)
        view = AuthorModelViewSet.as_view({'get':'list'})
        response = view(request)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_factory_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post(self.url,self.authors_dict,format=self.format)
        view = AuthorModelViewSet.as_view({'post':'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_factory_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post(self.url,self.authors_dict,format=self.format)
        force_authenticate(request,self.admin)
        view = AuthorModelViewSet.as_view({'post':'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_api_client_detail(self):
        # APIClient
        client = APIClient()
        response = client.get(f'{self.url}{self.authors.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_api_client_update_guest(self):
        client = APIClient()
        response = client.put(f'{self.url}{self.authors.id}/',**self.authors_dict_fake)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    def test_api_client_update_admin(self):
        client = APIClient()
        client.force_authenticate(user=self.admin)
        response = client.put(f'{self.url}{self.authors.id}/',
                              self.authors_dict_fake,format=self.format)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.authors.refresh_from_db()
        self.assertEqual(self.authors.first_name,self.authors_dict_fake.get('first_name'))
        self.assertEqual(self.authors.last_name,self.authors_dict_fake.get('last_name'))
        self.assertEqual(self.authors.birthday_year,self.authors_dict_fake.get('birthday_year'))
        client.logout()


    def tearDown(self) -> None:
        pass


class TestMath(APISimpleTestCase):

    def test_sqrt(self):
        import math
        response = math.sqrt(4)
        self.assertEqual(response,2)



class TestBiography(APITestCase):
    def setUp(self) -> None:
        self.url = '/api/biographies/'
        self.authors_dict = {'first_name':'Александр','last_name':'Пушкин','birthday_year':1799}
        self.authors_dict_fake = {'first_name':'Имя','last_name':'Фамилия','birthday_year':2000}
        self.format = 'json'
        # self.login = 'admin'
        # self.password = 'admin__12345678'
        # self.admin = User.objects.create_superuser(self.login,'admin@mail.ru',self.password)
        self.authors = Author.objects.create(**self.authors_dict)
        self.authors_new = Author.objects.create(**self.authors_dict_fake)
        self.biographies_dict = {'text': 'Test', 'author':self.authors}
        self.biographies_dict_fake = {'text': 'change text', 'author':self.authors_new.id}
        self.biographies = Biographies.objects.create(**self.biographies_dict)


    def test_api_test_case_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_api_test_case_update_admin(self):
        admin = User.objects.create_superuser('admin', 'admin@admin.com',
                                              'admin_12345678')

        self.client.login(username='admin', password='admin_12345678')
        response = self.client.put(f'{self.url}{self.biographies.id}/',
                              self.biographies_dict_fake)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

        self.biographies.refresh_from_db()
        self.assertEqual(self.biographies.text,self.biographies_dict_fake.get('text'))
        self.assertEqual(self.biographies.author.id,self.biographies_dict_fake.get('author'))
        self.client.logout()



    def test_mixer(self):
        bio = mixer.blend(Biographies,text='DEVELOPER')
        self.client.force_authenticate(user=self.admin)

        response = self.client.put(f'{self.url}{bio.id}/',
                                   self.biographies_dict_fake)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        bio.refresh_from_db()
        self.assertEqual(bio.text,
                         self.biographies_dict_fake.get('text'))
        self.assertEqual(bio.author.id,
                         self.biographies_dict_fake.get('author'))
        self.client.logout()

    def tearDown(self) -> None:
        pass