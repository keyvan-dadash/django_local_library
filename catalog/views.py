from django.shortcuts import render,get_object_or_404,reverse
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Book,Author,BookInstance
from .Catalog_Views.Index import Index
from .Catalog_Views.BookListView import BookListView
from .Catalog_Views.LoanListView import LoanListView
from .Catalog_Views.BookDetailViews import BookDetailViews
from .Catalog_Views.AuthorCreate import AuthorCreate
from .Catalog_Views.AuthorUpdate import AuthorUpdate
from .Catalog_Views.AuthorDelete import AuthorDelete
from .forms import ReNewBookForm
import datetime

@login_required
def renew_book(request, pk):
    book_ins = get_object_or_404(BookInstance, pk=pk)
    if request.method == 'POST' :
        form = ReNewBookForm(request.POST)

        if form.is_valid():
            book_ins.due_back = form.cleaned_data['renewal_date']
            book_ins.save()
            return HttpResponseRedirect(reverse('catalog:borrowed-book'))

    else :
        default = datetime.date.today() + datetime.timedelta(weeks=3)
        form = ReNewBookForm(initial={'renewal_date':default})

    return render(request, 'catalog/book_renew.html', {'form':form, 'book_ins':book_ins})
