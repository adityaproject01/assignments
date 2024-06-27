from django.shortcuts import render
from .models import User,Book
from django.http import HttpResponse
from django .contrib.auth.hashers import make_password,check_password
from rest_framework.views import APIView
# Create your views here.

from django.shortcuts import render
from .models import Book
from rest_framework.views import APIView
from rest_framework.response import Response

class BooksLists(APIView):
    def get(self, request):
        books = Book.objects.all()
        book_titles = []  

        for book in books:
            book_titles.append(book.title)  
        return Response(book_titles)  

class AddBook(APIView):
    def post(self,request):
        title=request.data.get("title")
        category=request.data.get("category")
        language=request.data.get("language")
        quantity=request.data.get("quantity")
        price=request.data.get("price")
        author=request.data.get("author")
        publicationDate=request.data.get("publicationDate")
        isbn=request.data.get("isbn")
        image=request.POST.get('image')
        book=Book.objects.create(title=title,category=category,language=language,quantity=quantity,price=price,author=author,publicationDate=publicationDate,isbn=isbn,image=image)
        return HttpResponse(book)
class AddUser(APIView):
    def post(self,request):
        name=request.data.get("name")
        email=request.data.get("email")
        phone=request.data.get("phone")
        password=make_password(request.data.get("password"))
        address=request.data.get("address")
        if User.objects.filter(email=email).exists():
            return HttpResponse("user already exist")
        try:
            user=User.objects.create(name=name,email=email,password=password,address=address,phone=phone)
            return HttpResponse(user,'message,Data received successfully')
        except Exception as e:
            return HttpResponse(str(e))
