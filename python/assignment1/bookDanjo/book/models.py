from django.db import models


class User(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.IntegerField(default=10)
    password=models.CharField(max_length=255)
    address=models.TextField()


class Book(models.Model):
    title=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    language=models.CharField(max_length=255)
    quantity=models.IntegerField(default=2)
    price=models.IntegerField(default=2)
    author=models.CharField(max_length=255)
    publicationDate=models.DateField()
    isbn=models.CharField(max_length=10,default=10)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    # blank unique null 

class Author(models.Model):
    authorName=models.CharField(max_length=255)

class OrderDate(models.Model):
    bookName=models.CharField(max_length=255)
    


