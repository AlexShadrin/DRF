
from django.urls import path

from userapp.views import UserListAPIView
app_name = 'userapp'

urlpatterns = [

    path('', UserListAPIView.as_view()),

]