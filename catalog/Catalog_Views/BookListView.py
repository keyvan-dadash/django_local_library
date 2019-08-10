from django.shortcuts import render
from django.views import generic
from catalog.models import Book,Author,BookInstance
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin
import json


class BookListView(LoginRequiredMixin,generic.ListView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_list = Book.objects.all()
        tmpjson = serializers.serialize("json",book_list,use_natural_foreign_keys=True, use_natural_primary_keys=True)
        tmpobj = json.loads(tmpjson)
        context['book_list'] = tmpjson
        return context
