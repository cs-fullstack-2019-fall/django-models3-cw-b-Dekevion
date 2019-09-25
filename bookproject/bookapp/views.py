from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
from .models import Book

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def makeBook(request):
    Book3 = Book(name ='book',pageNumber = 22, genre = 'fiction',publishDate = '2018-06-06')
    Book2 = Book(name = "No aedi", pageNumber = 20, genre = 'fiction', publishDate ='2016-01-01')
    Book2.save()
    Book3.save()
    return HttpResponse('You added a book')

def allBooks(request):
    allNames = Book.objects.all()

    for i in allNames:
        print(i.name)
    return HttpResponse('printed all entry names')
def pubDate(request):
    allDates = Book.objects.all()

    for x in allDates:
        if x.publishDate > datetime.date(2018,1,1):
            print(x.publishDate)
    return HttpResponse('Print only dates > current date')
