from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Book, Author, BookInstance, Genre, Language
from django.views.generic import CreateView, DetailView

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    
    return render(
        request,
        'catalog/index.html',
        context={
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
        }
    )

class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    initial = {'language': 'English'}

class BookDetailView(DetailView):
    model = Book
    