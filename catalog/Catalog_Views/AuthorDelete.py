from django.views import generic
from ..Catalog_Models import Author
from django.urls import reverse_lazy
class AuthorDelete(generic.DeleteView):
    model        = Author
    success_url  = reverse_lazy('catalog:books')
