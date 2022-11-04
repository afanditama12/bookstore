from django.shortcuts import render
from django.http import HttpResponse
# import models Book
from .models import Book

# Create your views here.

# this is a view for listing all the books
def home(request):
    return HttpResponse('Home Page')

# this is a view for listing a single book,it will take id as an argument
def book_detail(request, id):
    return HttpResponse('Book Detail')

# this is a list for adding a book
def add_book(request):
    return HttpResponse('Add Book')

# this is a view for editing the book's info
def edit_book(request):
    return HttpResponse('Edit Book')

# this is a view for deleting a book,it will take id as an argument
def delete_book(request, id):
    return HttpResponse('Delete Book')