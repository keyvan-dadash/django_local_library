from django.views import generic
from ..Catalog_Models import Author
class AuthorCreate(generic.CreateView):
    model    = Author
    fields   = '__all__'
    initial  = {'date_of_death':'05/01/2018'}
