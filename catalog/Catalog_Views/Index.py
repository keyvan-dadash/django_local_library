from django.shortcuts import render
from django.views import generic
from catalog.models import Book,Author,BookInstance
from django.contrib.auth.mixins import LoginRequiredMixin

class Index(LoginRequiredMixin,generic.TemplateView):
    template_name = 'catalog/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['num_books'] = Book.objects.all().count()
        context['num_authors'] = Author.objects.count()
        context['num_instances'] = BookInstance.objects.all().count()
        context['num_instances_available'] = BookInstance.objects.filter(status__exact='a').count()
        context['username'] = self.request.user.username
        return context



















# def index(request):
#     num_books = Book.objects.all().count()
#     num_authors = Author.objects.count()
#     num_instances = BookInstance.objects.all().count()
#     num_instances_available = BookInstance.objects.filter(status__exact='a').count()
#
#     return render(request,
#     'catalog/index.html',
#     context={'num_books':num_books,'num_authors':num_authors,'num_instances':num_instances,'num_instances_available':num_instances_available,}
#     )
