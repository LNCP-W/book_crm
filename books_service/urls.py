"""
URL configuration for BooksCRM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from .views import AllBooks,ExistedBooks,SoldBook, SoldBooks,  Book, CreateBook, CreateAuthor, DeleteBookView, CreatePublisher, AuthorView, PublisherView, AllAuthorsView, AllPublishersView

urlpatterns = [
    path('all/', AllBooks.as_view(), name='all_books'),
    path('sold/', SoldBooks.as_view(), name='sold_books'),
    path('', ExistedBooks.as_view(), name='existed_books'),
    path('<int:pk>/', Book.as_view(), name='book_detail'),
    path('sold/<int:pk>/', SoldBook.as_view(), name='sold_book'),
    path('author/<int:pk>/', AuthorView.as_view(), name='author'),
    path('publisher/<int:pk>/', PublisherView.as_view(), name='publisher'),
    path('<int:pk>/edit', Book.as_view(), name='edit_book'),
    path('create', CreateBook.as_view(), name='create_book'),
    path('author/create', CreateAuthor.as_view(), name='create_author'),
    path('author/all', AllAuthorsView.as_view(), name='all_authors'),
    path('publisher/all', AllPublishersView.as_view(), name='all_publishers'),
    path('publisher/create', CreatePublisher.as_view(), name='create_publisher'),
    path('delete/<int:pk>', DeleteBookView.as_view(), name='delete_book'),

]
