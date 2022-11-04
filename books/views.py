from django.shortcuts import render, redirect
# from django.http import HttpResponse
# import models Book
from .models import Book

# Create your views here.

# this is a view for listing all the books
def home(request):
    # retrieving all the books from the database
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books/home.html', context)

# this is a view for listing a single book,it will take id as an argument
def book_detail(request, id):
    # querying a particular book by its id
    book = Book.objects.get(pk=id)
    context = {'book': book}
    return render(request, 'books/book-detail.html', context)

# this is a list for adding a book
def add_book(request):
    # checking if the method is POST
    if request.method == 'POST':
        # getting all the data from the POST request
        data = request.POST
        # getting the image
        image = request.FILES.get('image-file')
        # creating and saving the book
        book = Book.objects.create(
           title = data['title'],
           author = data['author'],
           isbn = data['isbn'],
           price = data['price'],
           image = image
        )
        # going to the home page
        return redirect('home')
    return render(request, 'books/add-book.html')

# this is a view for editing the book's info
def edit_book(request):
    return HttpResponse('Edit Book')

# this is a view for deleting a book,it will take id as an argument
def delete_book(request, id):
    return HttpResponse('Delete Book')