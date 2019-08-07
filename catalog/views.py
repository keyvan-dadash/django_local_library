from django.shortcuts import render
from django.views import generic
from .models import Book,Author,BookInstance
from .Catalog_Views.Index import Index
from .Catalog_Views.BookListView import BookListView
