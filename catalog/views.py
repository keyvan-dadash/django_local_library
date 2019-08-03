from django.shortcuts import render

from .models import Book,Author,BookInstance

def index(request):
    num_books = Book.objects.all().count()
    num_authors = Author.objects.count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    return render(request,
    'catalog/index.html',
    context={'num_books':num_books,'num_authors':num_authors,'num_instances':num_instances,'num_instances_available':num_instances_available,}
    )
