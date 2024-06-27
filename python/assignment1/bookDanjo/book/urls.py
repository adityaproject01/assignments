from django.urls import path
from .views import *

urlpatterns = [
    path('book/', BooksLists.as_view(), name='book' ),
    path('addBooks/',AddBook.as_view(),name='addBooks'),
    path('addUser/',AddUser.as_view(),name='user')
]
