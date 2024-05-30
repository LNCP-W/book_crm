from datetime import datetime
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Books, Author, Publisher
from .forms import BookForm, AuthorForm, PublisherForm
from .utils import get_book_image, get_author_img
from django.core.files.base import ContentFile, File

# Create your views here.

class AllBooks(ListView):
    model = Books
    paginate_by = 5

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', 'name')
        # validate ordering here
        return [ordering, ]

class ExistedBooks(ListView):
    model = Books
    template_name = 'books_service/existed_list_tamplate.html'
    def get_queryset(self,*args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(price_out=None)

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', 'name')
        # validate ordering here
        return [ordering, ]


class SoldBooks(ListView):
    model = Books
    template_name = 'books_service/sold_list_tamplate.html'
    def get_queryset(self,*args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        return qs.exclude(price_out=None)

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', 'name')
        # validate ordering here
        return [ordering, ]


class Book(DetailView):
    model = Books

class AuthorView(DetailView):
    model = Author
    def get(self, *args, **kwargs):
        c=1
        return super().get(*args, **kwargs)

class CreateBook(CreateView):
    form_class = BookForm
    success_url = reverse_lazy("all_books")
    template_name = 'books_service/books_form.html'

    def get_context_data(self, **kwargs):
        context = super(CreateBook, self).get_context_data(**kwargs)
        context['authors'] = Author.objects.all()
        context['publishers'] = Publisher.objects.all()
        return context

    def form_valid(self, form):
        if not form.instance.picture:
            name, content = get_book_image(form.instance.name)
            if name:
                form.instance.picture.save(name, ContentFile(content))
        return super().form_valid(form)


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if kwargs.get('data'):
            kwargs['data']._mutable = True
            kwargs['data']['bought'] = datetime.today().date()
            author, _saved = Author.objects.get_or_create(name=kwargs['data']['author'])
            if _saved:
                name, content = get_author_img(author.name)
                if name:
                    author.picture.save(name, ContentFile(content))
            kwargs['data']['author'] = author.id
            publisher, _saved = Publisher.objects.get_or_create(name=kwargs['data']['publisher'])
            kwargs['data']['publisher'] = publisher.id
            kwargs['data']._mutable = False
        return kwargs

class CreateAuthor(CreateView):
    form_class = AuthorForm
    success_url = reverse_lazy("all_books")
    template_name = 'books_service/author_form.html'


class CreatePublisher(CreateView):
    form_class = PublisherForm
    success_url = reverse_lazy("all_books")
    template_name = 'books_service/publisher_form.html'

class PublisherView(DetailView):
    model = Publisher

class AllPublishersView(ListView):
    model = Publisher

class AllAuthorsView(ListView):
    model = Author

class DeleteBookView(DeleteView):
    model = Books
    success_url = reverse_lazy("all_books")

class SoldBook(UpdateView):
    model = Books
    fields = ["price_out"]
    template_name = 'books_service/sold_form.html'
    success_url = reverse_lazy("existed_books")
