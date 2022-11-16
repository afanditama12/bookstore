from django.shortcuts import render, redirect

from django.http import HttpResponse

# import models Book
from .models import Book

# import EditBookForm
from .forms import EditBookForm

# import user from django models library
from django.contrib.auth.models import User

# import django messages
from django.contrib import messages

# import authenticate, login, logout
from django.contrib.auth import authenticate, login, logout

# import login required from django decorators
from django.contrib.auth.decorators import login_required


# Create your views here.

# this is view for login
def loginPage(request):
    # checking if the method is POST
    if request.method == "POST":
        # get username data
        username = request.POST.get("username")
        # get password data
        password = request.POST.get("password")

        # check if user exist or not
        try:
            # get data from username
            user = User.objects.get(username=username)
        except:
            # if user not exist
            messages.error(request, "User doesn't exist.")

        # if user does exist
        user = authenticate(request, username=username, password=password)

        # check if user not empty/none
        if user is not None:
            # user success login
            login(request, user)
            return redirect("home")
        else:
            # if user not login
            messages.error(request, "Username or Password doesn't exist.")

    context = {}
    return render(request, "books/login_register.html", context)


# this is a view for logout
def logoutPage(request):
    # send data request of process logout
    logout(request)
    # if logout success
    return redirect('home')


# this is a view for listing all the books
def home(request):
    # retrieving all the books from the database
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "books/home.html", context)


# this is a view for listing a single book,it will take id as an argument
def book_detail(request, id):
    # querying a particular book by its id
    book = Book.objects.get(pk=id)
    context = {"book": book}
    return render(request, "books/book-detail.html", context)

# add decorator for restricted user
@login_required(login_url='login')
# this is a list for adding a book
def add_book(request):
    # checking if the method is POST
    if request.method == "POST":
        # getting all the data from the POST request
        data = request.POST
        # getting the image
        image = request.FILES.get("image-file")
        # creating and saving the book
        book = Book.objects.create(
            title=data["title"],
            author=data["author"],
            isbn=data["isbn"],
            price=data["price"],
            image=image,
        )
        # going to the home page
        return redirect("home")
    return render(request, "books/add-book.html")


# this is a view for editing the book's info
def edit_book(request, id):
    # getting the book to be updated
    book = Book.objects.get(pk=id)
    # populating the form with the book's information
    form = EditBookForm(instance=book)
    # checking if the request is POST
    if request.method == "POST":
        # filling the form with all the request data
        form = EditBookForm(request.POST, request.FILES, instance=book)
        # checking if the form's data is valid
        if form.is_valid():
            # saving the data to the database
            form.save()
            # redirecting to the home page
            return redirect("home")
    context = {"form": form}
    return render(request, "books/update-book.html", context)


# this is a view for deleting a book,it will take id as an argument
def delete_book(request, id):
    # getting the book to be deleted
    book = Book.objects.get(pk=id)
    # checking if the method is POST
    if request.method == "POST":
        # delete the book
        book.delete()
        # return to home after a success delete
        return redirect("home")
    context = {"book": book}
    return render(request, "books/delete-book.html", context)
