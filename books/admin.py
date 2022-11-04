from django.contrib import admin
from .models import Book

# Register your models here.
# registering the Book to the admin site
admin.site.register(Book)