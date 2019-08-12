from django.shortcuts import render
from django.views import generic
from catalog.models import Book,Author,BookInstance
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin
import json


class LoanListView(LoginRequiredMixin,generic.ListView):
    model               = BookInstance
    paginate_by         = 10
    template_name       = "catalog/Loan_List.html"
    context_object_name = "loan_list"


    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
