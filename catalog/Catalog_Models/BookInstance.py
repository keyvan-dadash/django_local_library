from django.db import models
import uuid
from . import Book
from django.contrib.auth.models import User
from datetime import date

class BookInstance(models.Model):

    id        = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique id for this book")
    book      = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint   = models.CharField(max_length=200)
    due_back  = models.DateField(blank=True, null=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status      = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text="book status")
    borrower    = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return "%s (%s)" % (self.id,self.book.title)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False
