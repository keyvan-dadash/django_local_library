from django.shortcuts import render
from django.views import generic
from catalog.models import Book,Author,BookInstance
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin
import json


class BookDetailViews(LoginRequiredMixin,generic.DetailView):
    model = Book
    template_name = "catalog/book_detail.html"
    context_object_name = 'book_detail'
