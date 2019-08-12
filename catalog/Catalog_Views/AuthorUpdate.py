from django.views import generic
from ..Catalog_Models import Author

class AuthorUpdate(generic.UpdateView):
    model   = Author
    fields  = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
