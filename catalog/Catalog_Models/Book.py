from django.db import models
from django.urls import reverse
from . import Author,Genre


class Book(models.Model):

    #Book have manytomany relation with Genre
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    summary = models.CharField(max_length=1000)
    isnb = models.CharField(max_length=13, help_text="Enter 13 char isbn")

    genre = models.ManyToManyField('Genre', help_text="Enter genres for this book")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
