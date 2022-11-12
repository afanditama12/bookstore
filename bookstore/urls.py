"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# importing the django's in-built admin url
from django.contrib import admin

# importing path and include from django's in-built urls
from django.urls import path, include

# importing conf from settings.py
from django.conf import settings

# importing conf.urls from static
from django.conf.urls.static import static

# importing views from subproject
from django.contrib.auth import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # registering books application's urls in project
    path("bookstore/", include("books.urls")),
]

# appending the urls with the static urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
